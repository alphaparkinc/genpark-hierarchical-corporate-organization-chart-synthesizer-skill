from client import HierarchicalCorporateOrganizationChartSynthesizerClient

def main():
    client = HierarchicalCorporateOrganizationChartSynthesizerClient()
    res = client.synthesize_organization_chart('Autonomous AI Systems Inc', 80, 3)
    print('Corporate Org Chart Synthesizer: ' + res['org_chart_id'] + ' (' + res['company'] + ')')
    print('Headcount: ' + str(res['total_headcount_mapped']) + ' | Span of Control: ' + str(res['span_of_control_ratio']))
    print('Hierarchy Verified: ' + str(res['acyclic_reporting_hierarchy_verified']))
    print('Interactive SVG: ' + res['interactive_svg_hierarchy_url'])
    print('HRMS CSV: ' + res['hrms_compatible_csv_url'])

if __name__ == '__main__':
    main()
