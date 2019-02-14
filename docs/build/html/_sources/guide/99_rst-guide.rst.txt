==================================================
Appendix 3: reStructuredText Help
==================================================

  :ref:`the-reference`


This section provides an overview of the style and reStructuredText (rST) used in this document. More comprehensive guides exist for rST, such as the `rST Specifications <http://docutils.sourceforge.net/docs/ref/rst/restructuredtext.html>`_ or `Sphinx docs <http://www.sphinx-doc.org/en/master/usage/restructuredtext/basics.html>`_.  But here we provide just a quick overview and reference for the typical usage found in this guide.

rST is somewhat similar to Markdown, but it has more features. However, rST can be more complex.  In particular, the header structure is somewhat more confusing.

You can compare the guide's source code with the rendered output to help get a better idea.
Otherwise online live-rendering tools are useful for practicing.  For example, you could copy the source for this page and take it over to `rst.ninjs.org <http://rst.ninjs.org>`_.

.. tip::

  Alternatively, you can examine the source code for other projects to see their use of rST, such as:

  **Pylons**

  `ReadTheDocs - Pylons <https://docs.pylonsproject.org/projects/docs-style-guide/>`_

  `Source code on GitHub - Pylons <https://github.com/Pylons/docs-style-guide/tree/master/docs>`_

  **Datasette**

  `ReadTheDocs - Datasette <https://datasette.readthedocs.io/en/stable/>`_

  `Source code on GitHub - Datasette <https://github.com/simonw/datasette/blob/master/docs/>`_

--------------------------------------------------

Headers
==================================================

In rST, there is no set pattern for creating headers.
Instead, the header patterns are essentially derived from the order.
So the first style encountered will be an outermost title (like HTML H1), the second style will be a subtitle, the third will be a subsubtitle, and so on.

This automatic creation of header styles can make it a bit confusing to understand what header you're actually typing. And if you don't understand that, you can get weird results.

So this guide tends to use this approach to the headers:

- a Title (or H1) pattern for the top of the page
- a Section (or H2) pattern to mark out sections
- a Subsection (or H3) pattern to mark out subsections
- a Sub-subsection (or H4) pattern to mark out sub-subsections
- etc

Now that we know the order is important, we can realise that the symbols used are less important.

That said, we use the following convention to help standardise this guide.

.. note::

  The symbols used in this convention are not important for the output.
  Instead, they provide a quick understanding for collaborative guide writers as to what was intended.

  The length of the underline must be at least as long as the title itself.
  If an under and overline are used, their length must be identical (eg. for the H1).

  To standardise the source code in this guide, we use a length of **50 chars** for the underlines.
  A header exceeding that length should be rare.

::

  ==================================================
  Heading 1 - for Page Titles (ie. "=" above & below)
  ==================================================`

  Heading 2 - for Section Marking
  ==================================================

  Heading 3 - for
  --------------------------------------------------

  This is a heading 4
  ..................................................

  This is a heading 5
  ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~



--------------------------------------------------

Paragraphs
==================================================

Paragraphs are simply written as plain text.
If you write on the next line, it is automatically added to that paragraph.

To create a new paragraph just add a line space between the sentences.

--------------------------------------------------

Indentation
==================================================

Indentation can be used to indicate block quotes, definitions (in definition list items), and local nested content:

Here is some text
  Here is some indented text.
    Then we indent it some more

Then we remove it all

--------------------------------------------------


Inline markup
==================================================

Inline markup features used most often are italics, bold, and code.
::

  *Italic text* is surrounded by 1x asterisk.
  **Bold text** is surrounded by 2x asterisks.
  `Interpreted text` is surrounded by 1x backtick.
  ``inline code`` is surrounded by 2x backticks.


--------------------------------------------------

Separators
==================================================

A horizontal line can be created by using 4 or more "-" in a row.
::

  ----

This renders like html's <hr>.

--------------------------------------------------


Literal Blocks
==================================================

A paragraph consisting of two colons "::" signifies that the following text block(s) comprise a literal block. The literal block must either be indented or quoted. No markup processing is done within a literal block. It is left as-is, and is typically rendered in a monospaced typeface:

Here is an example of literal blocks:
::

  ::

    Two colons are added,then a blank line
    Then the text is indented, and it will print out in monospace.
    Each additional line must also be indented.
    When you want to stop the literal block, just un-indent a new line.

Literal blocks can be used to quickly render code:
::

  ::

    py -m venv env


--------------------------------------------------

Inline Code
==================================================


Inline code snippets are written with double backticks before and after the text.
For example:
We then run the command: ````$ python -m venv env````

This renders as:

We then run the command: ``$ python -m venv env``

--------------------------------------------------

Code-Blocks
==================================================

Code-blocks can also be used to render different coding languages.
To do that, use the format:
::

  .. code-block:: languagename

  For example:
  .. code-block:: html
  .. code-block:: sql
  .. code-block:: python

And to add line numbers, you can use ``:linenos:``:
::

  .. code-block:: html
     :linenos:

Here's an a code-block formatted with html, with numbers
::

  .. code-block:: html
     :linenos:

     <h1>Code Block with Numbers</h1>
     <p>some more code</p>

This would render as follows:

.. code-block:: html
   :linenos:

    <h1>Code Block with Numbers</h1>
    <p>some more code</p>

Here's a code-block formatted for sql, without numbers
::

   .. code-block:: sql

      SELECT * FROM TABLE django_auth

Here's a code-block using specific emphasis
::

  .. code-block:: python
     :emphasize-lines: 3,5

     def some_function():
         interesting = False
         print 'This line is highlighted.'
         print 'This one is not...'
         print '...but this one is.'

This renders as:

.. code-block:: python
   :emphasize-lines: 3,5

   def some_function():
       interesting = False
       print 'This line is highlighted.'
       print 'This one is not...'
       print '...but this one is.'

Links
==================================================

Links can be written simply in the normal form, as shown here:
::

  http://djangomeetup.com

However if you want the link to be replaced by text, add some backticks, the text, angle brackets around the link, and an underscore at the end:
::

  `Django Meetup <http://djangomeetup.com>`_

This renders as
`Django Meetup <http://djangomeetup.com>`_

We can thereafter use the reference text to repeatedly refer to that link.
We do this by using that same text, surrounded by backticks and a final underscore.
::

`Django Meetup`_

This then renders as
`Django Meetup`_


--------------------------------------------------

Bullet Lists
==================================================

Bullet lists can be written with a "*", "-", or "+".
New lines can be added below each list point, but keep the indenting the same to keep it matched with that point.

::

    Bullet List 1
    ----------------------------------------------
    * A bulleted list item.
      You can add a new line, but make sure to indent it
    * Second list item.

    Bullet List 2
    ----------------------------------------------
    - A bulleted list item.
    - Second list item.

--------------------------------------------------

Enumerated Lists
==================================================

Enumerated lists use the "#." format.
Here are some examples:

::

    Enumerated List 1
    ----------------------------------------------
    #. This is a numbered list.
    #. It has three items.
    #. The last item.

You can nest lists, but you must leave a blank line above the first nested list point:
::

    Enumerated List 2 - Nested
    ----------------------------------------------
    #. This is a numbered list.
     * this is a nested sub-point
     * this is another sub-point
    #. It has three items.

    * this is a nested sub-point
    #. The last item.

       * this is a nested sub-point

The numbered list renders as follows:

#. This is a numbered list

 - this is a nested sub-point
 - this is another sub-point

#. It has three items

 * this is a nested sub-point

#. The last item.

 * this is a nested sub-point

--------------------------------------------------

Images
==================================================

Graphics can be in either the form images, or figures.
For example, here's how an image may be placed:
::

  .. image:: _static/images/logo.png

A figure (a graphic with a caption) may placed like this:
::

  .. figure:: _static/images/directory-structure.png

     Directory Structure


--------------------------------------------------

Directives
==================================================

.. _the-reference:

This part is a reference.


