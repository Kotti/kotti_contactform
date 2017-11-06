History
=======

0.6 - Unreleased
----------------

- Fix the unicode encode issue in mail submission.


0.5.1 - 2016-05-25
------------------

- Allows to override templates in other addon. [castaf]

0.5 - 2014-11-11
----------------

- Migrate to Bootstrap 3.
  This requires ``Kotti>=0.10b1`` and is a **backward incompatible change if you have customized any template**!

0.4.1 - 2014-11-11
------------------

- Fix the RecaptchaWidget serializer that hasn't been working at all before.

0.4 - 2014-11-11
----------------

- Integrate optional captcha service for the contact form.
- Require Kotti>=0.9.2
- Add an additional sender column.
  Using the user supplied email address as the mail sender fails if the sender domain has an SPF record and the receiving mail server checks SPF records.
  You need to run the migration script or add the column yourself (on SQLite).

0.3 - 2013-11-01
----------------

- Added frech translation. [jon1012]

0.2 - 2013-01-07
----------------

- Implement IDefaultworkflow.
- Add an additional one column layout for the contact form view.
- Use decorators for view config.
- Add fanstatic filter to development.ini.

0.1.1 - 2012-12-28
------------------

- Changes for compatibility with Kotti>=0.8. These changes
  are not backward compatible. If you want to use kotti_contactform
  with Kotti<=0.7.x then pin to 0.1.1a5.
- Use form classes for the form views instead of deprecated generic functions.
- Use pyramid.includes instead of deprecated kotti.includes.

0.1.1a5 - 2012-08-21
--------------------

- Use alembic environment of Kotti for upgrades.
- Depend on Kotti >0.7

0.1.1a4 - 2012-07-28
--------------------

- Fixed source distribution package.

0.1.1a3 - 2012-07-28
--------------------

- Changed class row to row-fluid in contact form template.
- Added Japanese translation.

0.1.1a2 - 2012-06-28
--------------------

- Fixed source distribution package.

0.1.1a1 - 2012-06-27
--------------------

- Attachment as optional setting.
- Added database migration with alembic.

0.1.0b4 - 2012-05-21
--------------------

- Changed layout.
- Added possibility for attachments.

0.1.0b3 - 2012-03-16
--------------------

- Update models to use Declarative for compatibility with Kotti >= 0.6.
