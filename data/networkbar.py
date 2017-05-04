# Load data for networkbar

import sys
from hascore.models import db, NetworkLink

if __name__ == '__main__':

    db.session.add_all([
        NetworkLink(seq=1, name=u'home', title=u'HasGeek', url=u'http://hasgeek.com/'),
        NetworkLink(seq=2, name=u'blog', title=u'Blog', url=u'http://blog.hasgeek.com/'),
        NetworkLink(seq=3, name=u'jobs', title=u'Jobs', url=u'http://jobs.hasgeek.com/'),
        NetworkLink(seq=4, name=u'hgtv', title=u'TV', url=u'http://hasgeek.tv/'),
        NetworkLink(seq=5, name=u'funnel', title=u'Funnel', url=u'http://funnel.hasgeek.com/'),
        NetworkLink(seq=6, name=u'geekup', title=u'Geekup', url=u'http://geekup.in/'),
        NetworkLink(seq=7, name=u'hacknight', title=u'Hacknight', url=u'http://hacknight.in/'),
        ])

    events = NetworkLink(seq=8, name=u'events', title=u'Events')
    workshops = NetworkLink(seq=9, name=u'workshops', title=u'Workshops')
    db.session.add_all([events, workshops])

    db.session.add_all([
        NetworkLink(seq=20, parent=events, name=u'fifthelephant', title=u'The Fifth Elephant',
            url=u'http://fifthelephant.in/'),
        NetworkLink(seq=21, parent=events, name=u'pastevents', title=u'Past events', sep=True),
        NetworkLink(seq=22, parent=events, name=u'metarefresh', title=u'Meta Refresh',
            url=u'http://metarefresh.in/'),
        NetworkLink(seq=23, parent=events, name=u'jsfoo', title=u'JSFoo',
            url=u'http://jsfoo.in/'),
        NetworkLink(seq=24, parent=events, name=u'droidcon', title=u'Droidcon',
            url=u'http://droidcon.in/'),
        NetworkLink(seq=25, parent=events, name=u'cartonama', title=u'Cartonama Conference',
            url=u'http://cartonama.com/2012'),
        NetworkLink(seq=26, parent=events, name=u'rootconf', title=u'Rootconf',
            url=u'http://rootconf.in/'),
        NetworkLink(seq=27, parent=events, name=u'phpcloud', title=u'Scaling PHP in the Cloud',
            url=u'http://phpcloud.hasgeek.com/'),
        NetworkLink(seq=28, parent=events, name=u'androidcamp', title=u'AndroidCamp',
            url=u'http://androidcamp.hasgeek.com/'),
        NetworkLink(seq=29, parent=events, name=u'doctypehtml5', title=u'DocType HTML5',
            url=u'http://www.doctypehtml5.in/'),
        ])
    db.session.add_all([
        NetworkLink(seq=50, parent=workshops, name=u'advancedpython', title=u'Advanced Python',
            url=u'http://advancedpython.hasgeek.com/'),
        NetworkLink(seq=51, parent=workshops, name=u'pastworkshops', title=u'Past workshops', sep=True),
        NetworkLink(seq=52, parent=workshops, name=u'gitworkshop', title=u'Git Workshop',
            url=u'http://gitworkshop.hasgeek.com/'),
        NetworkLink(seq=53, parent=workshops, name=u'pigworkshop', title=u'Pig Workshop',
            url=u'http://pigworkshop.fifthelephant.in/'),
        NetworkLink(seq=54, parent=workshops, name=u'cssforthesoul', title=u'CSS for the Soul',
            url=u'http://cssworkshop.metarefresh.in/'),
        NetworkLink(seq=55, parent=workshops, name=u'cartonamaworkshop', title=u'Cartonama Workshop',
            url=u'http://workshop.cartonama.com/'),
        ])
    db.session.commit()
