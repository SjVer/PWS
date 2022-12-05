from django.contrib.auth.decorators import login_required
from django.http import HttpRequest
from django.shortcuts import render
from django.conf import settings

from datetime import datetime
from locale import setlocale, LC_TIME

from .. import via_loading_page, with_error_message
from ...magister import get_session
from ... import figure_out

setlocale(LC_TIME, "nl_NL.utf8")

@login_required
@via_loading_page("Boeken")
@with_error_message("De boeken konden niet geladen worden.")
def boeken_page(request: HttpRequest):
	session = get_session(request)
	session.require_userinfo()
	subjects = figure_out.subjects(session)

	return render(request, "views/boeken.html", {
		"settings": settings,
		"title": "Boeken",
		"full_name": session.user.get_full_name(),
		"date": datetime.now().strftime("%A %-d %B"),
		"subjects": subjects,
	})