


html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
</head>
<body>
"""
strtemp = """
<style> body{
    background-color: aqua;
}</style>
<ul>{% for _ in string_list  %} <li><h2>{{ _ }}</h2></li>{% endfor%}</ul>
"""
strtemp1 = """
{% if username %} <h1> {{ username}} </h1>
{% else %} <h1> no name! </h1>
{% endif %}
"""
end = """
</body>
</html>
"""