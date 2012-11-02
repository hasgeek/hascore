from datetime import datetime, date
from flask import url_for
from coaster.views import jsonp, requestargs
from hascore import app


@app.route('/1/events/get')
def events_list():
    """
    List all upcoming events.
    """
    return jsonp({
        'profiles': {
            'off7nXRQQ7-S1ZK-D_tIdQ': {
                'name': 'droidconin',
                'title': 'Droidcon India',
                'buid': 'off7nXRQQ7-S1ZK-D_tIdQ',
                },
            },
        'workspaces': {
            'Mg8vrAAlSIanvE3qsZu2Dg': {
                'profile_id': 'off7nXRQQ7-S1ZK-D_tIdQ',
                'buid': 'Mg8vrAAlSIanvE3qsZu2Dg',
                'name': '2012',
                'title': 'Droidcon India 2012',
                'short_title': '2012',
                'feature_flags': ['funnel', 'schedule'],
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
                        'start': datetime(2012, 11, 2, 3, 30, 0).isoformat() + 'Z',
                        'end': datetime(2012, 11, 3, 12, 30, 0).isoformat() + 'Z',
                        'data_api_url': url_for('schedule_list',
                            profile='off7nXRQQ7-S1ZK-D_tIdQ', workspace='Mg8vrAAlSIanvE3qsZu2Dg',
                            _external=True)
                        }
                    }
                }
            }
        })


@app.route('/1/schedules/get_by_name')
@requestargs('event')
def schedule_by_name(event):
    """
    List schedules for requested event.
    """
    if event != 'droidconin/2012':
        return jsonp(status='error', error='unknown-event', description="No such event. Use profile/workspace syntax")

    # Return static data for Droidcon
    return schedule_list(profile='off7nXRQQ7-S1ZK-D_tIdQ', workspace='Mg8vrAAlSIanvE3qsZu2Dg')


@app.route('/1/schedules/get')
@requestargs('profile', 'workspace')
def schedule_list(profile, workspace):
    """
    List schedules for requested profile/workspace
    """
    if profile != 'off7nXRQQ7-S1ZK-D_tIdQ':
        return jsonp(status='error', error='unknown-profile', description="No such profile. Use the buid")
    if workspace != 'Mg8vrAAlSIanvE3qsZu2Dg':
        return jsonp(status='error', error='unknown-workspace', description="No such workspace. Use the buid")
    return jsonp()
