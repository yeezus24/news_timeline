from flask import Flask, render_template, request

app = Flask(__name__)

strs = ""

from GoogleNews import GoogleNews

def find_the_news(search):
	list_of_articles = []
	googlenews = GoogleNews()
	googlenews.setlang('en')
	googlenews.setperiod('d')
	# mm/dd/yyyy
	googlenews.setTimeRange('02/01/2020', '02/05/2020')

	googlenews.search(search)
	googlenews.getpage(1)
	result = googlenews.result()
	for i in result:
		list_of_articles.append(i)
	return list_of_articles


@app.route("/")
def news():
	return render_template('home.html')

@app.route('/result', methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form.to_dict(flat=False)
		result = result['Name'][0]
		return_list = find_the_news(result)
		return render_template('results.html', result = return_list)

if __name__ == "__main__":
	app.run(debug=True)