{
    'name': 'SaaS Portal',
    'version': '1.0.0',
    'author': 'Avalos Corp',
    'category': 'SaaS',
    'website': 'https://it-projects.info',
    'depends': ['oauth_provider', 'website', 'auth_signup', 'saas_base', 'saas_utils', 'base_action_rule'],
    'data': [
        'data/mail_template_data.xml',
        'data/plan_sequence.xml',
        'data/base_action_rule.xml',
        'data/cron.xml',
        'views/wizard.xml',
        'views/saas_portal.xml',
        'views/res_config.xml',
        'data/ir_config_parameter.xml',
        'data/subtype.xml',
        'data/support_team.xml',
        'views/res_users.xml',
        'data/res_users.xml',
        'data/base_action_rule.xml',
        'views/try_trial_template.xml',
        ],
    'installable': True,
}
