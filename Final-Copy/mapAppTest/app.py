from flask import Flask
from flask import render_template_string
from flask import render_template
import folium

app = Flask(__name__)

@app.route("/")
def fullscreen():
    """Embed a map as an iframe on a page."""
    m = folium.Map()

    m.get_root().width = "800px"
    m.get_root().height = "600px"
    iframe = m.get_root()._repr_html_()

    return render_template("home.html", iframe = iframe)


# @app.route("/iframe")
# def iframe():
#     """Embed a map as an iframe on a page."""
#     m = folium.Map()

#     m.get_root().width = "800px"
#     m.get_root().height = "600px"
#     iframe = m.get_root()._repr_html_()

#     return render_template_string("home.html", iframe)


# @app.route("/components")
# def components():
#     """Extract map components and put those on a page."""
#     m = folium.Map(
#         width=800,
#         height=600,
#     )

#     m.get_root().render()
#     header = m.get_root().header.render()
#     body_html = m.get_root().html.render()
#     script = m.get_root().script.render()

#     return render_template_string(
#         """
#             <!DOCTYPE html>
#             <html>
#                 <head>
#                     {{ header|safe }}
#                 </head>
#                 <body>
#                     <h1>Using components</h1>
#                     {{ body_html|safe }}
#                     <script>
#                         {{ script|safe }}
#                     </script>
#                 </body>
#             </html>
#         """,
#         header=header,
#         body_html=body_html,
#         script=script,
#     )
    

if __name__ == "__main__":
    my_port = 5133
    app.run(host='0.0.0.0', port = my_port, debug=True) 