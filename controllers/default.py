# -*- coding: utf-8 -*-

# init setutp

if not GPIO.getmode():
        GPIO.setmode(GPIO.BCM)
for pin in ALL_PIN:
    if GPIO.gpio_function(pin) !=0:
        GPIO.setup(pin,GPIO.OUT)
        GPIO.output(pin,GPIO.LOW)

def test():    
    scheduler.queue_task('stop_current', pvars=dict(all_pins=ALL_PIN),start_time=request.now + timed(seconds=30),timeout = 60)
    action=request.args[0]
    to_return='test'
    if action=='a_up':
        to_return='Ultima azione: alzo tutte le tapparelle {}'.format(ALL_PIN)
        all_up()
    elif action=='s_all':
        stop_all()
        to_return='Ultima azione: ferma tutto'
    elif action=='a_dw':
        all_dw()
        to_return='Ultima azione:  abbasso tutte le tapparelle'
    elif action=='m_up':
        mansarda_up()
        to_return='Ultima azione: alzo le tapparelle della mansarda'
    elif action=='m_dw':
        mansarda_dw()
        to_return='Ultima azione: abbasso le tapparelle della mansarda'    
    else:
        to_return='Azione non ancora supportata'
        print action

    return "jQuery('#target').html('{}');".format(to_return)

def index():
    #pass
    return dict(message=T('Prova domotica'))


def user():
    """
    exposes:
    http://..../[app]/default/user/login
    http://..../[app]/default/user/logout
    http://..../[app]/default/user/register
    http://..../[app]/default/user/profile
    http://..../[app]/default/user/retrieve_password
    http://..../[app]/default/user/change_password
    http://..../[app]/default/user/bulk_register
    use @auth.requires_login()
        @auth.requires_membership('group name')
        @auth.requires_permission('read','table name',record_id)
    to decorate functions that need access control
    also notice there is http://..../[app]/appadmin/manage/auth to allow administrator to manage users
    """
    return dict(form=auth())


@cache.action()
def download():
    """
    allows downloading of uploaded files
    http://..../[app]/default/download/[filename]
    """
    return response.download(request, db)


def call():
    """
    exposes services. for example:
    http://..../[app]/default/call/jsonrpc
    decorate with @services.jsonrpc the functions to expose
    supports xml, json, xmlrpc, jsonrpc, amfrpc, rss, csv
    """
    return service()
