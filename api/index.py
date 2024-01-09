from flask import Flask
app = Flask(__name__)

template_html = """
<html>
	<head>
		<meta content="自分で調べることはとても大切です。人に聞く前に自分で調べましょう。" property="og:description" />
	</head>
	<script>
		let redirectTo = "%redirect_to%";
		location.href = redirectTo;
	</script>
</html>
"""

@app.route("/")
def index():
	return template_html.replace("%redirect_to%", "https://www.google.com/")

@app.route("/<query>")
def search(query):
	query = query.replace(" ", "").replace("+", " ")
	return template_html.replace("%redirect_to%", f"https://www.google.com/search?q={query}")