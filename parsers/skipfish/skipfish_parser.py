"""
This is just a sample of algorithm which I am going to use to parse Skipfish result data from the file samples.js
I am using js2py python library to convert javascript to python
Currently I have just converted the javascript to python completely, solving the issue (as written in proposal)
in js2py (see line 105)
Later it can be used as required
"""
import re
import js2py

issue_desc = {
    
    "10101": "SSL certificate issuer information",
    "10201": "New HTTP cookie added",
    "10202": "New 'Server' header value seen",
    "10203": "New 'Via' header value seen",
    "10204": "New 'X-*' header value seen",
    "10205": "New 404 signature seen",

    "10401": "Resource not directly accessible",
    "10402": "HTTP authentication required",
    "10403": "Server error triggered",
    "10404": "Directory listing enabled",
    "10405": "Hidden files / directories",

    "10501": "All external links",
    "10502": "External URL redirector",
    "10503": "All e-mail addresses",
    "10504": "Links to unknown protocols",
    "10505": "Unknown form field (can't autocomplete)",
    "10601": "HTML form (not classified otherwise)",
    "10602": "Password entry form - consider brute-force",
    "10603": "File upload form",
    "10701": "User-supplied link rendered on a page",
    "10801": "Incorrect or missing MIME type (low risk)",
    "10802": "Generic MIME used (low risk)",
    "10803": "Incorrect or missing charset (low risk)",
    "10804": "Conflicting MIME / charset info (low risk)",
    "10901": "Numerical filename - consider enumerating",
    "10902": "OGNL-like parameter behavior",
    "10909": "Signature match (informational)",

    "20101": "Resource fetch failed",
    "20102": "Limits exceeded, fetch suppressed",
    "20201": "Directory behavior checks failed (no brute force)",
    "20202": "Parent behavior checks failed (no brute force)",
    "20203": "IPS filtering enabled",
    "20204": "IPS filtering disabled again",
    "20205": "Response varies randomly, skipping checks",
    "20301": "Node should be a directory, detection error?",

    "30101": "HTTP credentials seen in URLs",
    "30201": "SSL certificate expired or not yet valid",
    "30202": "Self-signed SSL certificate",
    "30203": "SSL certificate host name mismatch",
    "30204": "No SSL certificate data found",
    "30205": "Weak SSL cipher negotiated",
    "30206": "Host name length mismatch (name string has null byte)",
    "30301": "Directory listing restrictions bypassed",
    "30401": "Redirection to attacker-supplied URLs",
    "30402": "Attacker-supplied URLs in embedded content (lower risk)",
    "30501": "External content embedded on a page (lower risk)",
    "30502": "Mixed content embedded on a page (lower risk)",
    "30503": "HTTPS form submitting to a HTTP URL",
    "30601": "HTML form with no apparent XSRF protection",
    "30602": "JSON response with no apparent XSSI protection",
    "30603": "Auth form leaks credentials via HTTP GET",
    "30701": "Incorrect caching directives (lower risk)",
    "30801": "User-controlled response prefix (BOM / plugin attacks)",
    "30901": "HTTP header injection vector",
    "30909": "Signature match detected",

    "40101": "XSS vector in document body",
    "40102": "XSS vector via arbitrary URLs",
    "40103": "HTTP response header splitting",
    "40104": "Attacker-supplied URLs in embedded content (higher risk)",
    "40105": "XSS vector via injected HTML tag attribute",
    "40201": "External content embedded on a page (higher risk)",
    "40202": "Mixed content embedded on a page (higher risk)",
    "40301": "Incorrect or missing MIME type (higher risk)",
    "40302": "Generic MIME type (higher risk)",
    "40304": "Incorrect or missing charset (higher risk)",
    "40305": "Conflicting MIME / charset info (higher risk)",
    "40401": "Interesting file",
    "40402": "Interesting server message",
    "40501": "Directory traversal / file inclusion possible",
    "40601": "Incorrect caching directives (higher risk)",
    "40701": "Password form submits from or to non-HTTPS page",
    "40909": "Signature match detected (higher risk)",

    "50101": "Server-side XML injection vector",
    "50102": "Shell injection vector",
    "50103": "Query injection vector",
    "50104": "Format string vector",
    "50105": "Integer overflow vector",
    "50106": "File inclusion",
    "50107": "Remote file inclusion",
    "50201": "SQL query or similar syntax in parameters",
    "50301": "PUT request accepted",
    "50909": "Signature match detected (high risk)"

}
rfi = open("./samples.js", 'r')
file_read = rfi.read()
rfi.close()
# solving the issue I have talked about in proposal
# 1. take out each variable name and store them in a list
# 2. split the data at every ";"
# 3. then give each splitted data to js2py
# 4. then map them to vatiables from list.
pattern = re.compile(r"var\s+(?P<variables>[a-zA-Z_0-9]+)\s+(?==)")
variables = pattern.findall(file_read)
split_data = file_read.split(";")
js_data = [f for f in split_data if f is not None]
format_data = {}
py_data = []
for data in js_data:
	if js2py.eval_js(data) is not None:
		py_data.append(js2py.eval_js(data))
for i in range(len(py_data)):
	format_data[variables[i]] = py_data[i]
output_file = open("./output2.txt", 'w')
output_file.write(str(format_data))
output_file.close()

