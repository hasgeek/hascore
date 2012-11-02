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
    return jsonp({
        'venues': {
            'avi14aHLQruydl9b_03ORA': {
                'buid': 'avi14aHLQruydl9b_03ORA',
                'title': 'MLR Convention Centre, Whitefield',
                'location': {  # GeoJSON geometry object
                    'type': 'Point',
                    'coordinates': [12.9991, 77.7021],
                    },
                'rooms': {
                    'eXUTAdkvSEe0b2BL0tVWZw': {
                        'buid': 'eXUTAdkvSEe0b2BL0tVWZw',
                        'title': 'Auditorium'
                        },
                    'uEJqjqLIT9WqOGHF_E8LVQ': {
                        'buid': 'uEJqjqLIT9WqOGHF_E8LVQ',
                        'title': 'Banquet Hall'
                        },
                    'BDe5XDqHRP2qtblGp3bK6A': {
                        'buid': 'BDe5XDqHRP2qtblGp3bK6A',
                        'title': 'Discussion Room'
                        }
                    }
                }
            },
        'profiles': {
            'off7nXRQQ7-S1ZK-D_tIdQ': {
                'buid': 'off7nXRQQ7-S1ZK-D_tIdQ',
                'name': 'droidconin',
                'title': 'Droidcon India',
                },
            '4e9kRtq1RGGIkwQP2tYEjg': {
                'buid': '4e9kRtq1RGGIkwQP2tYEjg',
                'name': '4e9kRtq1RGGIkwQP2tYEjg',
                'title': 'Aravind Krishnaswamy',
                }
            },
        'workspaces': {
            'Mg8vrAAlSIanvE3qsZu2Dg': {
                'buid': 'Mg8vrAAlSIanvE3qsZu2Dg',
                'profile_id': 'off7nXRQQ7-S1ZK-D_tIdQ',
                'name': '2012',
                'title': 'Droidcon India 2012',
                'short_title': '2012',
                'timezone': 'Asia/Kolkata',
                'venues': ['avi14aHLQruydl9b_03ORA'],
                'sessions': [
                    {
                        'name': '596-about-droidcon-2012',
                        'title': 'About Droidcon 2012',
                        'description': None,
                        'room': 'eXUTAdkvSEe0b2BL0tVWZw',
                        'speakers': ['4e9kRtq1RGGIkwQP2tYEjg'],
                        'type': 'Panel',
                        'level': 'Beginner',
                        'start': datetime(2012, 11, 2, 4, 30, 0).isoformat() + 'Z',
                        'end': datetime(2012, 11, 2, 5, 0, 0).isoformat() + 'Z',
                        }
                    ]
                },
            },
        })
