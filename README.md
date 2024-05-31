<h1>CPSC 5021 Group Project</h1>

<h2>To-Do:</h2>
<ul>
  <li><s>Functions to calculate average rating and price in <code>app/models.py</code></s> BCE </li> 
  <li>Populate all reviews into the review forum page using the template provided in <code>app/views.py</code> and <code>app/templates/forum.html</code></li>
  <li>Populate reviews submitted by current user into the my reviews page using the template provided in <code>app/views.py</code> and <code>app/templates/my_reviews.html</code></li>
  <li>Implement search function in <code>app/views.py</code> for both wine library and review forum  -- Jason </li>
  <li>Implement filter function in <code>app/views.py</code> for my_reviews</li>
</ul>

Once the above is done:

<ul>
  <li>Copy the finished <code>library.html</code> into <code>wine_selection.html</code>, add a select bottom to each wine that links to post_review.html with the proper wine ID passed</li>
  <li>Link the rate this wine button in wine detail page to <code>post_review.html</code> with proper wine ID passed</li>
  <li>modify <code>app/views.py</code> and <code>app/urls.py</code> to properly link the wine selection page. (click on Rate Now should redirect user to wine selection page)</li>
  <li>Implement <code>post_review</code> function in <code>app/views.py</code> and update <code>app/templates/post_review.html</code> accordingly. If review exists for the wine-user combo passed in, populate post_review.html 
      with existing review and update existing review in the database. If review doesn't
      exist, create blank page and create new review in the database.</li>
</ul>

You should have direct access to this README file - please add your initial to the end of a task to mark the tasks you're working on or want to work on. use ~~this tag~~ to mark the tasks you've finished
