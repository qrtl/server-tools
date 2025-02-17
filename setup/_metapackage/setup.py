import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo14-addons-oca-server-tools",
    description="Meta package for oca-server-tools Odoo addons",
    version=version,
    install_requires=[
        'odoo14-addon-attachment_unindex_content',
        'odoo14-addon-auditlog',
        'odoo14-addon-auto_backup',
        'odoo14-addon-autovacuum_message_attachment',
        'odoo14-addon-base_cron_exclusion',
        'odoo14-addon-base_exception',
        'odoo14-addon-base_jsonify',
        'odoo14-addon-base_kanban_stage',
        'odoo14-addon-base_m2m_custom_field',
        'odoo14-addon-base_name_search_improved',
        'odoo14-addon-base_report_auto_create_qweb',
        'odoo14-addon-base_search_fuzzy',
        'odoo14-addon-base_sparse_field_list_support',
        'odoo14-addon-base_technical_user',
        'odoo14-addon-base_time_window',
        'odoo14-addon-base_view_inheritance_extension',
        'odoo14-addon-datetime_formatter',
        'odoo14-addon-excel_import_export',
        'odoo14-addon-excel_import_export_demo',
        'odoo14-addon-fetchmail_incoming_log',
        'odoo14-addon-fetchmail_notify_error_to_sender',
        'odoo14-addon-fetchmail_notify_error_to_sender_test',
        'odoo14-addon-html_image_url_extractor',
        'odoo14-addon-html_text',
        'odoo14-addon-letsencrypt',
        'odoo14-addon-module_auto_update',
        'odoo14-addon-module_change_auto_install',
        'odoo14-addon-onchange_helper',
        'odoo14-addon-sentry',
        'odoo14-addon-slow_statement_logger',
        'odoo14-addon-sql_export',
        'odoo14-addon-sql_export_excel',
        'odoo14-addon-sql_export_mail',
        'odoo14-addon-sql_request_abstract',
        'odoo14-addon-test_base_time_window',
        'odoo14-addon-upgrade_analysis',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
