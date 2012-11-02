from hascore import app


@app.route('/1/events')
def eventseries_list():
    """
    List all event series (limited to those with upcoming editions?).
    """
    pass


@app.route('/1/events/<eventseries>')
def eventeditions_list(eventseries):
    """
    List all (upcoming?) editions of an event.
    """
    pass


@app.route('/1/events/<eventseries>/editions/<edition>')
def eventedition_info():
    """
    List of rooms, slots and sessions in a given event edition.
    """
    pass


# Ugh! Make this /1/sessions/<sessionid>
@app.route('/1/events/<eventseries>/editions/<edition>/sessions/<session>')
def session_info():
    """
    Detail on a given session at an event.
    """
    pass
