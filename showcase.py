#!/usr/bin/env python3

import bottle
import os.path

import data

# Threshold in days after which a project is considered inactive, based on its
# code/date_last_commit information. This should be around 180, but not shorter
# than the update frequency of the showcase as a whole.
ACTIVITY_THRESHOLD_DAYS = 270

# Text representation of the various maturity levels
MATURITY_LABEL = {
        0: "This project has not yet been evaluated by the C4DT Factory team.\n"
        "We will be happy to evaluate it upon request.",
        1: "Prototype",
        2: "Intermediate",
        3: "Mature",
        }

# Main Factory page
FACTORY_URL = "https://www.c4dt.org/factory/software/"

CATEGORIES = [
    ["Privacy", "Privacy Protection & Cryptography"],
    ["Blockchain", "Blockchains & Smart Contracts"],
    ["Verification", "Software Verification"],
    ["Security", "Device and System Security"],
    ["Learning", "Machine Learning"],
    ["Other", "Other"],
]

def is_active(project):
    active = None

    if 'code' in project and 'date_last_commit' in project['code']:
        import datetime

        date_last_commit = project['code']['date_last_commit']
        today = datetime.datetime.now()
        threshold = datetime.timedelta(days=ACTIVITY_THRESHOLD_DAYS)
        active = today - date_last_commit <= threshold

    return active

def find_project(project_id, lab_id=None):
    labs = data.load()

    if lab_id is not None and lab_id not in labs:
        bottle.abort(404, f"Lab '{lab_id}' does not exist")

    for l_id, l in labs.items():
        if lab_id is not None and l_id != lab_id: continue

        for p_id, p in l['projects'].items():
            if p_id != project_id: continue

            return {**p, 'p_id': p_id}, {**l, 'lab_id': l_id}

    bottle.abort(404, f"Project '{project_id}' does not exist")

def find_project_tabs(project_id):
    tabs = [ tab for tab in ["presentation", "background", "demo", "hands-on", "pilot", "app"]
             if os.path.isfile(os.path.join("views", "incubator", tab, project_id + ".tpl"))]
    return tabs + ["technical"]

@bottle.route('/robots.txt')
def server_robots():
    return bottle.static_file('robots.txt', root='./')

@bottle.route('/resources/<path:path>')
def server_resources(path):
    return bottle.static_file(path, root='./resources/')

@bottle.route('/')
def index():
    bottle.redirect(FACTORY_URL)

@bottle.route('/showcase')
def showcase_no_slash():
    bottle.redirect('/showcase/')

@bottle.route('/showcase/')
@bottle.view('projects')
def showcase():
    labs = data.load()

    return dict(labs=labs, is_active=is_active,
            maturity_label=MATURITY_LABEL, categories=CATEGORIES,
            find_project_tabs=find_project_tabs)

@bottle.route('/incubator/<project_id>')
def incubator_project(project_id):
    tabs = find_project_tabs(project_id)
    bottle.redirect('/incubator/' + project_id + "/" + tabs[0])

@bottle.route('/incubator/<project_id>/<tab>')
@bottle.view('incubator/tabs')
def incubator_project_tab(project_id, tab):
    project, lab = find_project(project_id)

    return dict(project=project, lab=lab,
                tab=tab, tabs=find_project_tabs(project_id),
                is_active=is_active, maturity_label=MATURITY_LABEL)

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
