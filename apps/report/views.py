from django.core.urlresolvers import reverse, reverse_lazy
from django.forms import model_to_dict
from django.http import JsonResponse
from django.shortcuts import render

from apps.ledger.models import Category, Node
from apps.report.forms import ReportSettingForm
from apps.report.models import ReportSetting
from awecounting.utils.helpers import save_qs_from_ko, get_dict
from awecounting.utils.mixins import group_required, SuperOwnerMixin, UpdateView


def get_trial_balance_data(company):
    root_categories = Category.objects.filter(company=company, parent=None)
    root = {'nodes': [], 'total_dr': 0, 'total_cr': 0, 'settings': model_to_dict(ReportSetting.objects.get(company=company))}
    del root['settings']['id']
    del root['settings']['company']
    for root_category in root_categories:
        node = Node(root_category)
        root['nodes'].append(node.get_data())
        root['total_dr'] += node.dr
        root['total_cr'] += node.cr
    root['settings_save_url'] = reverse('report:save_report_settings')
    return root


@group_required('Accountant')
def trial_balance_json(request):
    return JsonResponse(get_trial_balance_data(request.company))


@group_required('Accountant')
def trial_balance(request):
    data = get_trial_balance_data(request.company)
    context = {
        'data': data,
    }
    return render(request, 'trial_balance.html', context)


@group_required('Accountant')
def save_report_settings(request):
    filter_kwargs = {'company': request.company}
    return JsonResponse(save_qs_from_ko(ReportSetting, filter_kwargs, request.body))


class ReportSettingUpdateView(SuperOwnerMixin, UpdateView):
    model = ReportSetting
    form_class = ReportSettingForm
    success_url = reverse_lazy('home')
    template_name = 'report/report_setting.html'

    def get_object(self, queryset=None):
        return self.model.objects.get(company=self.request.company)

    def get_context_data(self, **kwargs):
        context = super(ReportSettingUpdateView, self).get_context_data(**kwargs)
        context['base_template'] = '_base_settings.html'
        context['setting'] = 'ReportSetting'
        return context


def get_subnode(node, name):
    return get_dict(node['nodes'], 'name', name)


def trading_account(request):
    rows = []
    data = get_trial_balance_data(request.company)
    income = get_subnode(data, 'Income')
    sales = get_subnode(income, 'Sales')
    rows.append(('Sales', sales['cr']))
    expenses = get_subnode(data, 'Expenses')
    purchases = get_subnode(expenses, 'Purchase')
    rows.append(('(Purchases)', purchases['dr']))
    direct_expenses = get_subnode(expenses, 'Direct Expenses')
    rows.append(('(Direct Expenses)', direct_expenses['dr']))
    rows.append(('Gross Profit', float(sales['cr']) - float(purchases['dr']) - float(direct_expenses['dr']), 'ul'))
    return render(request, 'trading_account.html', {'data': data, 'rows': rows})


def profit_loss(request):
    rows = []
    data = get_trial_balance_data(request.company)
    income = get_subnode(data, 'Income')
    sales = get_subnode(income, 'Sales')
    rows.append(('Sales', sales['cr']))
    direct_income = get_subnode(income, 'Direct Income')
    rows.append(('Other Direct Income', direct_income['cr']))
    expenses = get_subnode(data, 'Expenses')
    purchases = get_subnode(expenses, 'Purchase')
    rows.append(('(Purchases)', purchases['dr']))
    direct_expenses = get_subnode(expenses, 'Direct Expenses')
    rows.append(('(Direct Expenses)', direct_expenses['dr']))
    gross_profit = float(sales['cr']) + float(direct_income['cr']) - float(purchases['dr']) - float(direct_expenses['dr'])
    rows.append(('Gross Profit', gross_profit, 'ul'))
    indirect_income = get_subnode(income, 'Indirect Income')
    rows.append(('Indirect Income', indirect_income['cr']))
    indirect_expenses = get_subnode(expenses, 'Indirect Expenses')
    rows.append(('(Indirect Expenses)', indirect_expenses['dr']))
    net_profit = gross_profit + float(indirect_income['cr']) - float(indirect_expenses['dr'])
    rows.append(('Net Profit', net_profit, 'ul'))
    return render(request, 'profit_loss.html', {'data': data, 'rows': rows})


def dr_bal(node):
    return float(node['dr'] or 0) - (float(node['cr'] or 0))


def cr_bal(node):
    return float(node['cr'] or 0) - (float(node['dr'] or 0))


def balance_sheet(request):
    data = get_trial_balance_data(request.company)
    equity_rows = []
    liability_rows = []
    asset_rows = []

    equity = get_subnode(data, 'Equity')
    equity_rows.append(('Equity', cr_bal(equity)))

    liabilities = get_subnode(data, 'Liabilities')
    payables = get_subnode(liabilities, 'Account Payables')
    liability_rows.append(('Payables/Suppliers', cr_bal(payables)))
    taxes = get_subnode(liabilities, 'Duties & Taxes')
    liability_rows.append(('Duties & Taxes', cr_bal(taxes)))
    other_payables = get_subnode(liabilities, 'Other Payables')
    liability_rows.append(('Other Payables', cr_bal(other_payables)))
    liabilities_total = cr_bal(equity) + cr_bal(payables) + cr_bal(taxes) + cr_bal(other_payables)

    assets = get_subnode(data, 'Assets')
    cash_accounts = get_subnode(assets, 'Cash Accounts')
    asset_rows.append(('Cash in Hand', dr_bal(cash_accounts)))
    cash_equivalent = get_subnode(assets, 'Cash Equivalent Account')
    asset_rows.append(('Cash Equivalent', dr_bal(cash_equivalent)))
    bank_account = get_subnode(assets, 'Bank Account')
    asset_rows.append(('Bank Accounts', dr_bal(bank_account)))
    fixed_assets = get_subnode(assets, 'Fixed Assets')
    asset_rows.append(('Fixed Assets', dr_bal(fixed_assets)))
    tax_receivables = get_subnode(assets, 'Tax Receivables')
    asset_rows.append(('Tax Receivables', dr_bal(tax_receivables)))
    assets_total = dr_bal(cash_accounts) + dr_bal(cash_equivalent) + dr_bal(bank_account) + dr_bal(fixed_assets) + dr_bal(
        tax_receivables)

    return render(request, 'balance_sheet.html',
                  {'data': data, 'equities': equity_rows, 'liabilities': liability_rows, 'assets': asset_rows,
                   'liabilities_total': liabilities_total, 'assets_total': assets_total})
