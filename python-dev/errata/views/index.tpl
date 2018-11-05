<!doctype html>
<html lang="en">
  <head>
    <meta charset='utf-8'>
    <meta name='viewport' content="width=device-width, initial-scale=1">
    <link rel='stylesheet' href="//code.jquery.com/ui/1.12.1/themes/base/jquery-ui.css">
    <link rel='stylesheet' href="/static/css/index.css">
    <title>Math Errata</title>
  </head>
  <body>
    <div class="accordion">
      % for chapter in chapters:
      <h3>Chapter {{ chapter[0] }}</h3>
      <div class="nested-accordion">
        % for page in chapter[1]:
        <h3>Page {{page}}</h3>
        <div>
          <img />
        </div>
        % end
      </div>
      % end
    </div>
    <script src="https://code.jquery.com/jquery-1.12.4.js"></script>
    <script src="https://code.jquery.com/ui/1.12.1/jquery-ui.js"></script>
    <script src="/static/js/script.js"></script>
  </body>
</html>
