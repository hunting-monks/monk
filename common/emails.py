from django.core.mail import EmailMultiAlternatives
from django.template import Context
from django.template.loader import get_template

def sendEmail(subject, from_email, to_email_list, text_content, html_content=None, context_dict={}):
	"""
	python -m smtpd -n -c DebuggingServer localhost:1025
	e.g., sendEmail('S', a@monks.com, [b@gmail.com], 'email_created.txt', 'email_created.html', context_dict):
	"""
	text_content = get_template(text_content)
	html_content = get_template(html_content)
	d = Context(context_dict)

	text_content = text_content.render(d)
	msg = EmailMultiAlternatives(subject, text_content, from_email, to_email_list)

	if html_content:
		html_content = html_content.render(d)
		msg.attach_alternative(html_content, "text/html")
	msg.send()


def sendRendedEmail(subject, from_email, to_email_list, text_content, html_content):
	msg = EmailMultiAlternatives(subject, text_content, from_email, to_email_list)
	if html_content:
		msg.attach_alternative(html_content, "text/html")
	msg.send()

