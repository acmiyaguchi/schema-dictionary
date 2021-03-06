#!/usr/bin/env python3

# try using https://raw.githubusercontent.com/mozilla-services/mozilla-pipeline-schemas/generated-schemas/schemas/telemetry/main/main.4.bq
# as input

import sys
import json


HTML = """
<html>
<head>
    <link
      rel="stylesheet"
      type="text/css"
      href="style.css"
    />
</head>
<body>
<div class="container mx-auto">
    <h1>telemetry.main</h1>
    <p>This table represents a stable view of the main ping. It is updated daily.</p>
    <p>Schema: <a href="https://github.com/mozilla-services/mozilla-pipeline-schemas/blob/master/schemas/telemetry/main/main.4.schema.json">mozilla-pipeline-schemas</a></p>
    <p>Scheduling: <a href="https://github.com/mozilla/telemetry-airflow/blob/master/dags/main_summary.py">Airflow</a></p>

    <div class="container schema-browser mx-auto">
        <ul>
            {dict_html}
        </ul>
    </div>
</div>
</body>
</html>
"""


def get_node_html(node):
    node_html = f"<li>{node['name']}"
    if node.get('description'):
        node_html += f" <span class=\"less-important\">{node['description']}</span>"
    if node.get('fields'):
        node_html += "<ul>"
        for field in node['fields']:
            node_html += get_node_html(field)
        node_html += "</ul>"
    node_html += "</li>"
    return node_html


schema = json.loads(open(sys.argv[1]).read())
dict_html = ""
for section in schema:
    dict_html += get_node_html(section)

print(HTML.format(dict_html=dict_html))
