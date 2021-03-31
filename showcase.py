#!/usr/bin/env python3

import bottle

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

def is_active(project):
    active = None

    if 'code' in project and 'date_last_commit' in project['code']:
        import datetime

        date_last_commit = project['code']['date_last_commit']
        today = datetime.datetime.now()
        threshold = datetime.timedelta(days=ACTIVITY_THRESHOLD_DAYS)
        active = today - date_last_commit <= threshold

    return active

@bottle.route('/robots.txt')
def server_robots():
    return bottle.static_file('robots.txt', root='./')

@bottle.route('/resources/<filename>')
def server_resources(filename):
    return bottle.static_file(filename, root='./resources/')

@bottle.route('/')
def index():
    bottle.redirect(FACTORY_URL)

@bottle.route('/showcase/labs')
def labs_no_slash():
    bottle.redirect('/showcase/labs/')

@bottle.route('/showcase/labs/')
@bottle.view('labs')
def labs():
    return dict(labs=data.load())

@bottle.route('/showcase')
@bottle.route('/showcase/')
def showcase_main():
    bottle.redirect('/showcase/projects/')

@bottle.route('/showcase/projects')
def projects_no_slash():
    bottle.redirect('/showcase/projects/')

@bottle.route('/showcase/projects/')
@bottle.route('/showcase/projects/<lab_id>')
@bottle.view('projects')
def projects(lab_id=None):
    labs = data.load()
    if lab_id and lab_id not in labs:
        bottle.abort(404, f"Lab '{lab_id}' does not exist")

    return dict(labs=labs, selected_lab_id=lab_id, is_active=is_active,
            maturity_label=MATURITY_LABEL)

@bottle.route('/showcase/project/<lab_id>/<project_id>')
@bottle.view('project')
def project(lab_id, project_id):
    labs = data.load()

    if lab_id not in labs:
        bottle.abort(404, f"Lab '{lab_id}' does not exist")

    found_projects = [
            (p, l)
            for l_id, l in labs.items()
            for p_id, p in l['projects'].items()
            if l_id == lab_id
            if p_id == project_id
            ]

    nb_projects = len(found_projects)

    if nb_projects == 0:
        bottle.abort(404, f"Project '{project_id}' does not exist")
    elif nb_projects > 1:
        bottle.abort(404, f"Project '{project_id}' is ambiguous ({nb_projects} instances)")

    project, lab = found_projects[0]
    lab['lab_id'] = lab_id

    return dict(project=project, lab=lab, is_active=is_active,
            maturity_label=MATURITY_LABEL)

if __name__ == '__main__':
    bottle.run(host='0.0.0.0', port=8080, debug=True, reloader=True)
