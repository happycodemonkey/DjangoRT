import rt
from djangoRT_settings import RT_HOST, RT_UN, RT_PW, RT_QUEUE

class DjangoRt:
	
	def __init__(self):
		self.rtHost = RT_HOST
		self.rtUn = RT_UN
		self.rtPw = RT_PW

		if RT_QUEUE == 'RT_QUEUE' or RT_QUEUE == '':
			self.rtQueue = rt.ALL_QUEUES
		else:
			self.rtQueue = RT_QUEUE

		self.tracker = rt.Rt(self.rtHost, self.rtUn, self.rtPw, basic_auth=(self.rtUn, self.rtPw))
		self.tracker.login()

	def getUserTickets(self, userEmail):
		return self.tracker.search(Queue=rt.ALL_QUEUES, raw_query="Requestors='" + userEmail + "'", order='-LastUpdated')

	def getTicket(self, ticket_id):
		return self.tracker.get_ticket(ticket_id)

	def getTicketHistory(self, ticket_id):
		return self.tracker.get_history(ticket_id)

	# Returns the ticket id of the created ticket
	def createTicket(self, ticket):
		return self.tracker.create_ticket(Queue=RT_QUEUE, 
				Subject=ticket.subject, 
				Text=ticket.problem_description, 
				Requestors=ticket.requestor,
				Cc=",".join(ticket.cc))

	def replyToTicket(self, ticket_id, reply_text):
		return self.tracker.reply(ticket_id, text=reply_text)

	# Checks if the current user is a requestor or CC on the ticket
	# Also doesn't crap out if the user isn't logged in even though
	# we should be checking before calling this
	def hasAccess(self, ticket_id, user = None):
		if user and ticket_id:
			ticket = self.tracker.get_ticket(ticket_id)	
			if user in ticket.get('Requestors', '') or user in ticket.get('Cc', ''):
				return True

		return False
