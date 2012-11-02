from datetime import datetime, date
from coaster.views import jsonp
from hascore import app


@app.route('/1/events/get')
def events_list():
    """
    List all upcoming events.
    """
    return jsonp({
        'profiles': [{
            'name': 'droidconin',
            'title': 'Droidcon India',
            'buid': 'off7nXRQQ7-S1ZK-D_tIdQ',
            }],
        'workspaces': [{
            'profile_id': 'off7nXRQQ7-S1ZK-D_tIdQ',
            'name': '2012',
            'title': 'Droidcon India 2012',
            'short_title': '2012',
            'flags': ['funnel', 'schedule'],
            'features': {
                'artwork': {
                    'color_bg': '#ffffff',
                    'color_bg2': '#ffffff',
                    'color_fg': '#222',
                    'color_fg2': '#222',
                    'logo_url': None,
                    'cover_url': None
                    },
                'schedule': {
                    'date_location': '2 & 3 November, Bangalore',
                    'start_date': date(2012, 11, 2).isoformat(),
                    'end_date': date(2012, 11, 3).isoformat(),
                    'start': None,
                    'end': None,
                    }
                }
            }]
        })


@app.route('/1/schedules/get')
def eventeditions_list():
    """
    List schedules for requested event.
    """
    pass
