import webbrowser
import sublime, sublime_plugin

class OpenBrowserCommand(sublime_plugin.TextCommand):

	def run(self, edit, url):
		
		selection = ""
		for region in self.view.sel():
			selection += self.view.substr(region)

		webbrowser.open(url % selection)