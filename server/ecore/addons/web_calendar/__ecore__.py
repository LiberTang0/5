{
    'name': 'Web Calendar',
    'category': 'Hidden',
    'description':"""
eCore Web Calendar view.
==========================

""",
    'author': 'Avalos Corp., Valentino Lab (Kalysto)',
    'version': '2.0',
    'depends': ['web'],
    'data' : [
        'views/web_calendar.xml',
    ],
    'qweb': [
        'static/src/xml/*.xml',
    ],
    'auto_install': True
}
