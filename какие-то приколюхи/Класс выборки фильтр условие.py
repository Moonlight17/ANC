class TitleList(ListView):

	template_name = 'testing.html'
	context_object_name = 'context'

	def get_queryset(self):
		self.title = get_object_or_404(Spisok, id=self.kwargs['pk'])
		return TitleList.objects.filter(title=self.title)


	def get_context_data(self, **kwargs):
		# Call the base implementation first to get a context
		context = super(AncView, self).get_context_data(**kwargs)
		# Add in the publisher
		context['title'] = self.title
		return context