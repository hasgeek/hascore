# Load data for networkbar

from hascore.models import NetworkLink, db

if __name__ == '__main__':

    db.session.add_all(
        [
            NetworkLink(seq=1, name='home', title='Hasgeek', url='http://hasgeek.com/'),
            NetworkLink(
                seq=2, name='blog', title='Blog', url='http://blog.hasgeek.com/'
            ),
            NetworkLink(
                seq=3, name='jobs', title='Jobs', url='http://jobs.hasgeek.com/'
            ),
            NetworkLink(seq=4, name='hgtv', title='TV', url='http://hasgeek.tv/'),
            NetworkLink(
                seq=5, name='funnel', title='Funnel', url='http://funnel.hasgeek.com/'
            ),
            NetworkLink(seq=6, name='geekup', title='Geekup', url='http://geekup.in/'),
            NetworkLink(
                seq=7, name='hacknight', title='Hacknight', url='http://hacknight.in/'
            ),
        ]
    )

    events = NetworkLink(seq=8, name='events', title='Events')
    workshops = NetworkLink(seq=9, name='workshops', title='Workshops')
    db.session.add_all([events, workshops])

    db.session.add_all(
        [
            NetworkLink(
                seq=20,
                parent=events,
                name='fifthelephant',
                title='The Fifth Elephant',
                url='http://fifthelephant.in/',
            ),
            NetworkLink(
                seq=21, parent=events, name='pastevents', title='Past events', sep=True
            ),
            NetworkLink(
                seq=22,
                parent=events,
                name='metarefresh',
                title='Meta Refresh',
                url='http://metarefresh.in/',
            ),
            NetworkLink(
                seq=23,
                parent=events,
                name='jsfoo',
                title='JSFoo',
                url='http://jsfoo.in/',
            ),
            NetworkLink(
                seq=24,
                parent=events,
                name='droidcon',
                title='Droidcon',
                url='http://droidcon.in/',
            ),
            NetworkLink(
                seq=25,
                parent=events,
                name='cartonama',
                title='Cartonama Conference',
                url='http://cartonama.com/2012',
            ),
            NetworkLink(
                seq=26,
                parent=events,
                name='rootconf',
                title='Rootconf',
                url='http://rootconf.in/',
            ),
            NetworkLink(
                seq=27,
                parent=events,
                name='phpcloud',
                title='Scaling PHP in the Cloud',
                url='http://phpcloud.hasgeek.com/',
            ),
            NetworkLink(
                seq=28,
                parent=events,
                name='androidcamp',
                title='AndroidCamp',
                url='http://androidcamp.hasgeek.com/',
            ),
            NetworkLink(
                seq=29,
                parent=events,
                name='doctypehtml5',
                title='DocType HTML5',
                url='http://www.doctypehtml5.in/',
            ),
        ]
    )
    db.session.add_all(
        [
            NetworkLink(
                seq=50,
                parent=workshops,
                name='advancedpython',
                title='Advanced Python',
                url='http://advancedpython.hasgeek.com/',
            ),
            NetworkLink(
                seq=51,
                parent=workshops,
                name='pastworkshops',
                title='Past workshops',
                sep=True,
            ),
            NetworkLink(
                seq=52,
                parent=workshops,
                name='gitworkshop',
                title='Git Workshop',
                url='http://gitworkshop.hasgeek.com/',
            ),
            NetworkLink(
                seq=53,
                parent=workshops,
                name='pigworkshop',
                title='Pig Workshop',
                url='http://pigworkshop.fifthelephant.in/',
            ),
            NetworkLink(
                seq=54,
                parent=workshops,
                name='cssforthesoul',
                title='CSS for the Soul',
                url='http://cssworkshop.metarefresh.in/',
            ),
            NetworkLink(
                seq=55,
                parent=workshops,
                name='cartonamaworkshop',
                title='Cartonama Workshop',
                url='http://workshop.cartonama.com/',
            ),
        ]
    )
    db.session.commit()
