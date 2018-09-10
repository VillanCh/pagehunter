#!/usr/bin/env python
# coding:utf-8
"""
  Author:   --<>
  Purpose: 
  Created: 09/08/18
"""

import unittest

from .. import core

base1 = """







<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta name="defaultLanguage" content="en">
    <meta name="availableLanguages" content="en">

    

    <title>Register · PyPI</title>
    <meta name="description" content="The Python Package Index (PyPI) is a repository of software for the Python programming language.">

    <link rel="stylesheet" href="/static/css/warehouse.a1809af1.css">
    <link rel="stylesheet" href="/static/css/fontawesome.4b73fd92.css">
    <link rel="stylesheet" href="/static/css/regular.19624371.css">
    <link rel="stylesheet" href="/static/css/solid.f478cfb1.css">
    <link rel="stylesheet" href="/static/css/brands.1ea560bf.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400italic,600,600italic,700,700italic|Source+Code+Pro:500">
    <noscript>
      <link rel="stylesheet" href="/static/css/noscript.ea8974d1.css">
    </noscript>

    

    <link rel="icon" href="/static/images/favicon.6a76275d.ico" type="image/x-icon">

    <link rel="alternate" type="application/rss+xml" title="RSS: 40 latest updates" href="/rss/updates.xml">
    <link rel="alternate" type="application/rss+xml" title="RSS: 40 newest packages" href="/rss/packages.xml">
    

    <meta property="og:url" content="https://pypi.org/account/register/">
    <meta property="og:site_name" content="PyPI">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://pypi.org/static/images/twitter.c0030826.jpg">
    <meta property="og:title" content="Register">
    <meta property="og:description" content="The Python Package Index (PyPI) is a repository of software for the Python programming language.">

    <link rel="search" type="application/opensearchdescription+xml" title="PyPI" href="/opensearch.xml">

    
    <script
      src="https://cdn.ravenjs.com/3.26.2/raven.min.js"
      integrity="sha384-D6LXy67EIC102DTuqypxwQsTHgiatlbvg7q/1YAWFb6lRyZ1lIZ6bGDsX7jxHNKA"
      crossorigin="anonymous">
    </script>
    
    <script async
            data-ga-id="UA-55961911-1"
            data-sentry-frontend-dsn="https://3a67b35c9dc248a191d761410b095861@sentry.io/1231155"
            src="/static/js/warehouse.b56a7115.js">
    </script>
    
  <script async
  src="/static/js/vendor/zxcvbn.9cf6916d.js">
</script>

    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-55961911-1"></script>
    <script defer src="https://www.fastly-insights.com/insights.js?k=6a52360a-f306-421e-8ed5-7417d0d4a4e9&dnt=true"></script>
  </head>

  <body data-controller="viewport-toggle">
    

    <!-- Accessibility: this link should always be the first piece of content inside the body-->
    <a href="#content" class="skip-to-content">Skip to main content</a>

    <button class="button button--primary button--switch-to-mobile hidden" data-target="viewport-toggle.switchToMobile" data-action="viewport-toggle#switchToMobile">
      Switch to mobile version
    </button>

    <section id="sticky-notifications" class="stick-to-top js-stick-to-top">
      <!-- Add browser warning. Will show for ie9 and below -->
      <!--[if IE]>
      <div class="notification-bar notification-bar--danger">
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning:</span>
        </span>
        <span class="notification-bar__message">You are using an unsupported browser, upgrade to a newer version.</span>
      </div>
      <![endif]-->
      
      <noscript>
      <div class="notification-bar notification-bar--danger">
        
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning:</span>
        </span>
        <span class="notification-bar__message">Some features may not work without JavaScript. Please try enabling it if you encounter problems.</span>
      </div>
      </noscript>
    </section>

    
      <div data-html-include="/_includes/flash-messages/">
      </div>
    

    

    

    <header class="site-header ">
      <div class="site-container">
        <div class="split-layout">
          
          <div class="split-layout">
            <div>
              <a class="site-header__logo" href="/">
                <img alt="PyPI" src="/static/images/logo-small.6eef541e.svg">
              </a>
            </div>

            <form class="search-form search-form--primary" action="/search/">
              <div role="search">
                <label for="search" class="sr-only">Search PyPI</label>
                <input id="search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="">
                
                <button type="submit" class="search-form__button">
                  <i class="fa fa-search" aria-hidden="true"></i>
                  <span class="sr-only">Search</span>
                </button>
              </div>
            </form>
          </div>
          

          <div data-html-include="/_includes/current-user-indicator/">
            <nav id="user-indicator" class="horizontal-menu horizontal-menu--light horizontal-menu--tall" aria-label="Main navigation">
  <a class="horizontal-menu__link horizontal-menu__link--remove-on-mobile" href="/help/">Help</a>
  <a class="horizontal-menu__link horizontal-menu__link--remove-on-mobile" href="https://donate.pypi.org">Donate</a>
  <a class="horizontal-menu__link" href="/account/login/">Log in</a>
  <a class="horizontal-menu__link" href="/account/register/">Register</a>
</nav>
          </div>
        </div>
      </div>
    </header>

    
    <section class="mobile-search">
      <form class="search-form search-form--fullwidth" action="/search/">
        <div role="search">
          <label for="mobile-search" class="sr-only">Search PyPI</label>
          <input id="mobile-search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="">
          
          <button type="submit" class="search-form__button">
            <i class="fa fa-search" aria-hidden="true"></i>
            <span class="sr-only">Search</span>
          </button>
          </button>
        </div>
      </form>
    </section>
    

    <main id="content">
      
  
    
  

  <section class="horizontal-section">
    <div class="site-container">
      <h1 class="page-title">Create an account on PyPI</h1>

      <form method="POST" action="/account/register/" data-controller="password password-match password-strength-gauge">
        <input name="csrf_token" type="hidden" value="tS0Gwq1bJZfFQCf-A9vfS5-fzGoVKJ81fN-lAM2xsW4">

        

        <div class="form-group">
          <label for="full_name" class="form-group__label">Name</label>
          <input autofocus class="form-group__input" id="full_name" name="full_name" placeholder="Your name" required="required" tabindex="1" type="text" value="">
          
        </div>

        <div class="form-group">
          <label for="full_name" class="form-group__label">Email address</label>
          <input autocomplete="email" class="form-group__input" id="email" name="email" placeholder="Your email address" required="required" tabindex="2" type="email" value="">
          
        </div>

        
        <div class="form-group confirm-form">
          <label for="confirm_form" class="form-group__label">Confirm form</label>
          <input aria-hidden="true" class="form-group__input" id="confirm_form" name="confirm_form" type="text" value="">
        </div>

        <div class="form-group">
          <label for="username" class="form-group__label">Username</label>
          <input autocapitalize="off" autocomplete="username" autocorrect="off" class="form-group__input" id="username" name="username" placeholder="Select a username" required="required" spellcheck="false" tabindex="3" type="text" value="">
          
        </div>

        <div>
          <div class="form-group">
            <div class="split-layout">
              <label for="password" class="form-group__label">Password</label>
              <label for="show-password">
                <input data-action="change->password#togglePasswords" data-target="password.showPassword"
                  id="show-password" type="checkbox" tabindex="7">&nbsp;Show passwords
              </label>
            </div>
            
            <div>
              <input autocomplete="new-password" class="form-group__input" data-action="keyup-&gt;password-match#checkPasswordsMatch keyup-&gt;password-strength-gauge#checkPasswordStrength" data-target="password.password password-match.passwordMatch password-strength-gauge.password" id="new_password" name="new_password" placeholder="Select a password" required="required" tabindex="4" type="password" value="">
            </div>
            
            <p class="form-group__help-text">
  Choose a strong password that contains letters (uppercase and lowercase), numbers and special characters. Avoid common words or repetition.
</p>
<p class="form-group__help-text">
  <strong>Password strength:</strong>
  <span class="password-strength">
    <span class="password-strength__gauge" data-target="password-strength-gauge.strengthGauge">
      <span class="sr-only">Password field is empty</span>
    </span>
  </span>
</p>
          </div>

          <div class="form-group">
            <label for="password_confirm" class="form-group__label">Confirm password</label>
            <input class="form-group__input" data-action="keyup-&gt;password-match#checkPasswordsMatch" data-target="password.password password-match.passwordMatch" id="password_confirm" name="password_confirm" placeholder="Confirm password" required="required" tabindex="5" type="password" value="">
            
          </div>
        </div>

        <div class="form-group">
          <ul class="form-errors">
            <li data-target="password-match.matchMessage" class="hidden"></li>
          </ul>
        </div>

        <input type="submit" value="Create account" class="button button--primary" data-target="password-match.submit" tabindex="6">
      </form>
    </div>
  </section>

    </main>

    <footer class="footer" role="contentinfo">
      <div class="footer__logo">
        <img src="/static/images/white-cube.8c3a6fe9.svg" alt="Logo" class="-js-white-cube">
      </div>

      <div class="footer__menus">
        <ul class="footer__menu">
          <li>
            <h2>Help</h2>
          </li>
          <li><a href="https://packaging.python.org/installing/">Installing packages</a></li>
          <li><a href="https://packaging.python.org/distributing/">Uploading packages</a></li>
          <li><a href="https://packaging.python.org/">User guide</a></li>
          <li><a href="/help/">FAQs</a></li>
        </ul>
        <ul class="footer__menu">
          <li>
            <h2>About PyPI</h2>
          </li>
          
          <li><a href="https://status.python.org/">Status: <span data-statuspage-domain="https://2p66nmmycsj3.statuspage.io">all systems operational</span></a></li>
          
          <li><a href="https://dtdg.co/pypi">Infrastructure dashboard</a></li>
          <li><a href="https://www.python.org/dev/peps/pep-0541/">Package index name retention</a></li>
          <li><a href="/sponsors/">Our sponsors</a></li>
        </ul>


        <ul class="footer__menu">
          <li>
            <h2>Contributing to PyPI</h2>
          </li>
          <li><a href="/help/#feedback">Bugs and feedback</a></li>
          <li><a href="https://github.com/pypa/warehouse">Contribute on GitHub</a></li>
          <li><a href="https://github.com/pypa/warehouse/graphs/contributors">Development credits</a></li>
        </ul>
        <ul class="footer__menu">
          <li>
            <h2>Using PyPI</h2>
          </li>
          <li><a href="https://www.pypa.io/en/latest/code-of-conduct/">Code of conduct</a></li>
          <li><a href="/security/">Report security issue</a></li>
          <li><a href="https://www.python.org/privacy/">Privacy policy</a></li>
          <li><a href="/policy/terms-of-use/">Terms of use</a></li>
        </ul>
      </div>

      <hr class="footer__divider">

      <div class="footer__text">
        <p>
          Developed and maintained by the Python community, for the Python community.
          <br>
          <a href="https://donate.pypi.org">Donate today!</a>
        </p>
        <p>© 2018 <a href="https://www.python.org/psf/">Python Software Foundation</a></p>
      </div>

      <div class="centered hide-on-desktop">
        <button class="button button--switch-to-desktop hidden" data-target="viewport-toggle.switchToDesktop" data-action="viewport-toggle#switchToDesktop">
          Desktop version
        </button>
      </div>
    </footer>

    

<div class="sponsors">
  <p class="sponsors__title">Supported by</p>
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.elastic.co/">
        <img class="sponsors__image" alt="Elastic" src="/static/images/sponsors/white/elastic.a912fb87.png">
        <span class="sponsors__name">Elastic</span>
        <span class="sponsors__service">Search</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.pingdom.com/">
        <img class="sponsors__image" alt="Pingdom" src="/static/images/sponsors/white/pingdom.07446398.png">
        <span class="sponsors__name">Pingdom</span>
        <span class="sponsors__service">Monitoring</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://cloud.google.com/">
        <img class="sponsors__image" alt="Google" src="/static/images/sponsors/white/google.2f72f26f.png">
        <span class="sponsors__name">Google</span>
        <span class="sponsors__service">BigQuery</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://getsentry.com/for/python">
        <img class="sponsors__image" alt="Sentry" src="/static/images/sponsors/white/sentry.5ab437bc.png">
        <span class="sponsors__name">Sentry</span>
        <span class="sponsors__service">Error logging</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://aws.amazon.com/">
        <img class="sponsors__image" alt="AWS" src="/static/images/sponsors/white/aws.5f800271.png">
        <span class="sponsors__name">AWS</span>
        <span class="sponsors__service">Cloud computing</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.datadoghq.com/">
        <img class="sponsors__image" alt="DataDog" src="/static/images/sponsors/white/datadog.e569d741.png">
        <span class="sponsors__name">DataDog</span>
        <span class="sponsors__service">Monitoring</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.fastly.com/">
        <img class="sponsors__image" alt="Fastly" src="/static/images/sponsors/white/fastly.0563c6f5.png">
        <span class="sponsors__name">Fastly</span>
        <span class="sponsors__service">CDN</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.digicert.com/">
        <img class="sponsors__image" alt="DigiCert" src="/static/images/sponsors/white/digicert.79748718.png">
        <span class="sponsors__name">DigiCert</span>
        <span class="sponsors__service">EV certificate</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://statuspage.io">
        <img class="sponsors__image" alt="StatusPage" src="/static/images/sponsors/white/statuspage.67af0b3d.png">
        <span class="sponsors__name">StatusPage</span>
        <span class="sponsors__service">Status page</span>
      </a>
    
  
</div>

    
  </body>

</html>
"""

base2 = """







<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta name="defaultLanguage" content="en">
    <meta name="availableLanguages" content="en">

    

    <title>Register · PyPI</title>
    <meta name="description" content="The Python Package Index (PyPI) is a repository of software for the Python programming language.">

    <link rel="stylesheet" href="/static/css/warehouse.a1809af1.css">
    <link rel="stylesheet" href="/static/css/fontawesome.4b73fd92.css">
    <link rel="stylesheet" href="/static/css/regular.19624371.css">
    <link rel="stylesheet" href="/static/css/solid.f478cfb1.css">
    <link rel="stylesheet" href="/static/css/brands.1ea560bf.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400italic,600,600italic,700,700italic|Source+Code+Pro:500">
    <noscript>
      <link rel="stylesheet" href="/static/css/noscript.ea8974d1.css">
    </noscript>

    

    <link rel="icon" href="/static/images/favicon.6a76275d.ico" type="image/x-icon">

    <link rel="alternate" type="application/rss+xml" title="RSS: 40 latest updates" href="/rss/updates.xml">
    <link rel="alternate" type="application/rss+xml" title="RSS: 40 newest packages" href="/rss/packages.xml">
    

    <meta property="og:url" content="https://pypi.org/account/register/">
    <meta property="og:site_name" content="PyPI">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://pypi.org/static/images/twitter.c0030826.jpg">
    <meta property="og:title" content="Register">
    <meta property="og:description" content="The Python Package Index (PyPI) is a repository of software for the Python programming language.">

    <link rel="search" type="application/opensearchdescription+xml" title="PyPI" href="/opensearch.xml">

    
    <script
      src="https://cdn.ravenjs.com/3.26.2/raven.min.js"
      integrity="sha384-D6LXy67EIC102DTuqypxwQsTHgiatlbvg7q/1YAWFb6lRyZ1lIZ6bGDsX7jxHNKA"
      crossorigin="anonymous">
    </script>
    
    <script async
            data-ga-id="UA-55961911-1"
            data-sentry-frontend-dsn="https://3a67b35c9dc248a191d761410b095861@sentry.io/1231155"
            src="/static/js/warehouse.b56a7115.js">
    </script>
    
  <script async
  src="/static/js/vendor/zxcvbn.9cf6916d.js">
</script>

    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-55961911-1"></script>
    <script defer src="https://www.fastly-insights.com/insights.js?k=6a52360a-f306-421e-8ed5-7417d0d4a4e9&dnt=true"></script>
  </head>

  <body data-controller="viewport-toggle">
    

    <!-- Accessibility: this link should always be the first piece of content inside the body-->
    <a href="#content" class="skip-to-content">Skip to main content</a>

    <button class="button button--primary button--switch-to-mobile hidden" data-target="viewport-toggle.switchToMobile" data-action="viewport-toggle#switchToMobile">
      Switch to mobile version
    </button>

    <section id="sticky-notifications" class="stick-to-top js-stick-to-top">
      <!-- Add browser warning. Will show for ie9 and below -->
      <!--[if IE]>
      <div class="notification-bar notification-bar--danger">
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning:</span>
        </span>
        <span class="notification-bar__message">You are using an unsupported browser, upgrade to a newer version.</span>
      </div>
      <![endif]-->
      
      <noscript>
      <div class="notification-bar notification-bar--danger">
        
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning:</span>
        </span>
        <span class="notification-bar__message">Some features may not work without JavaScript. Please try enabling it if you encounter problems.</span>
      </div>
      </noscript>
    </section>

    
      <div data-html-include="/_includes/flash-messages/">
      </div>
    

    

    

    <header class="site-header ">
      <div class="site-container">
        <div class="split-layout">
          
          <div class="split-layout">
            <div>
              <a class="site-header__logo" href="/">
                <img alt="PyPI" src="/static/images/logo-small.6eef541e.svg">
              </a>
            </div>

            <form class="search-form search-form--primary" action="/search/">
              <div role="search">
                <label for="search" class="sr-only">Search PyPI</label>
                <input id="search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="">
                
                <button type="submit" class="search-form__button">
                  <i class="fa fa-search" aria-hidden="true"></i>
                  <span class="sr-only">Search</span>
                </button>
              </div>
            </form>
          </div>
          

          <div data-html-include="/_includes/current-user-indicator/">
            <nav id="user-indicator" class="horizontal-menu horizontal-menu--light horizontal-menu--tall" aria-label="Main navigation">
  <a class="horizontal-menu__link horizontal-menu__link--remove-on-mobile" href="/help/">Help</a>
  <a class="horizontal-menu__link horizontal-menu__link--remove-on-mobile" href="https://donate.pypi.org">Donate</a>
  <a class="horizontal-menu__link" href="/account/login/">Log in</a>
  <a class="horizontal-menu__link" href="/account/register/">Register</a>
</nav>
          </div>
        </div>
      </div>
    </header>

    
    <section class="mobile-search">
      <form class="search-form search-form--fullwidth" action="/search/">
        <div role="search">
          <label for="mobile-search" class="sr-only">Search PyPI</label>
          <input id="mobile-search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="">
          
          <button type="submit" class="search-form__button">
            <i class="fa fa-search" aria-hidden="true"></i>
            <span class="sr-only">Search</span>
          </button>
          </button>
        </div>
      </form>
    </section>
    

    <main id="content">
      
  
    
  

  <section class="horizontal-section">
    <div class="site-container">
      <h1 class="page-title">Create an account on PyPI</h1>

      <form method="POST" action="/account/register/" data-controller="password password-match password-strength-gauge">
        <input name="csrf_token" type="hidden" value="tS0Gwq1bJZfFQCf-A9vfS5-fzGoVKJ81fN-lAM2xsW4">

        

        <div class="form-group">
          <label for="full_name" class="form-group__label">Name</label>
          <input autofocus class="form-group__input" id="full_name" name="full_name" placeholder="Your name" required="required" tabindex="1" type="text" value="">
          
        </div>

        <div class="form-group">
          <label for="full_name" class="form-group__label">Email address</label>
          <input autocomplete="email" class="form-group__input" id="email" name="email" placeholder="Your email address" required="required" tabindex="2" type="email" value="">
          
        </div>

        
        <div class="form-group confirm-form">
          <label for="confirm_form" class="form-group__label">Confirm form</label>
          <input aria-hidden="true" class="form-group__input" id="confirm_form" name="confirm_form" type="text" value="">
        </div>

        <div class="form-group">
          <label for="username" class="form-group__label">Username</label>
          <input autocapitalize="off" autocomplete="username" autocorrect="off" class="form-group__input" id="username" name="username" placeholder="Select a username" required="required" spellcheck="false" tabindex="3" type="text" value="">
          
        </div>

        <div>
          <div class="form-group">
            <div class="split-layout">
              <label for="password" class="form-group__label">Password</label>
              <label for="show-password">
                <input data-action="change->password#togglePasswords" data-target="password.showPassword"
                  id="show-password" type="checkbox" tabindex="7">&nbsp;Show passwords
              </label>
            </div>
            
            <div>
              <input autocomplete="new-password" class="form-group__input" data-action="keyup-&gt;password-match#checkPasswordsMatch keyup-&gt;password-strength-gauge#checkPasswordStrength" data-target="password.password password-match.passwordMatch password-strength-gauge.password" id="new_password" name="new_password" placeholder="Select a password" required="required" tabindex="4" type="password" value="">
            </div>
            
            <p class="form-group__help-text">
  Choose a strong password that contains letters (uppercase and lowercase), numbers and special characters. Avoid common words or repetition.
</p>
<p class="form-group__help-text">
  <strong>Password strength:</strong>
  <span class="password-strength">
    <span class="password-strength__gauge" data-target="password-strength-gauge.strengthGauge">
      <span class="sr-only">Password field is empty</span>
    </span>
  </span>
</p>
          </div>

          <div class="form-group">
            <label for="password_confirm" class="form-group__label">Confirm password</label>
            <input class="form-group__input" data-action="keyup-&gt;password-match#checkPasswordsMatch" data-target="password.password password-match.passwordMatch" id="password_confirm" name="password_confirm" placeholder="Confirm password" required="required" tabindex="5" type="password" value="">
            
          </div>
        </div>

        <div class="form-group">
          <ul class="form-errors">
            <li data-target="password-match.matchMessage" class="hidden"></li>
          </ul>
        </div>

        <input type="submit" value="Create account" class="button button--primary" data-target="password-match.submit" tabindex="6">
      </form>
    </div>
  </section>

    </main>

    <footer class="footer" role="contentinfo">
      <div class="footer__logo">
        <img src="/static/images/white-cube.8c3a6fe9.svg" alt="Logo" class="-js-white-cube">
      </div>

      <div class="footer__menus">
        <ul class="footer__menu">
          <li>
            <h2>Help</h2>
          </li>
          <li><a href="https://packaging.python.org/installing/">Installing packages</a></li>
          <li><a href="https://packaging.python.org/distributing/">Uploading packages</a></li>
          <li><a href="https://packaging.python.org/">User guide</a></li>
          <li><a href="/help/">FAQs</a></li>
        </ul>
        <ul class="footer__menu">
          <li>
            <h2>About PyPI</h2>
          </li>
          
          <li><a href="https://status.python.org/">Status: <span data-statuspage-domain="https://2p66nmmycsj3.statuspage.io">all systems operational</span></a></li>
          
          <li><a href="https://dtdg.co/pypi">Infrastructure dashboard</a></li>
          <li><a href="https://www.python.org/dev/peps/pep-0541/">Package index name retention</a></li>
          <li><a href="/sponsors/">Our sponsors</a></li>
        </ul>


        <ul class="footer__menu">
          <li>
            <h2>Contributing to PyPI</h2>
          </li>
          <li><a href="/help/#feedback">Bugs and feedback</a></li>
          <li><a href="https://github.com/pypa/warehouse">Contribute on GitHub</a></li>
          <li><a href="https://github.com/pypa/warehouse/graphs/contributors">Development credits</a></li>
        </ul>
        <ul class="footer__menu">
          <li>
            <h2>Using PyPI</h2>
          </li>
          <li><a href="https://www.pypa.io/en/latest/code-of-conduct/">Code of conduct</a></li>
          <li><a href="/security/">Report security issue</a></li>
          <li><a href="https://www.python.org/privacy/">Privacy policy</a></li>
          <li><a href="/policy/terms-of-use/">Terms of use</a></li>
        </ul>
      </div>

      <hr class="footer__divider">

      <div class="footer__text">
        <p>
          Developed and maintained by the Python community, for the Python community.
          <br>
          <a href="https://donate.pypi.org">Donate today!</a>
        </p>
        <p>© 2018 <a href="https://www.python.org/psf/">Python Software Foundation</a></p>
      </div>

      <div class="centered hide-on-desktop">
        <button class="button button--switch-to-desktop hidden" data-target="viewport-toggle.switchToDesktop" data-action="viewport-toggle#switchToDesktop">
          Desktop version
        </button>
      </div>
    </footer>

    

<div class="sponsors">
  <p class="sponsors__title">Supported by</p>
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.elastic.co/">
        <img class="sponsors__image" alt="Elastic" src="/static/images/sponsors/white/elastic.a912fb87.png">
        <span class="sponsors__name">Elastic</span>
        <span class="sponsors__service">Search</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.pingdom.com/">
        <img class="sponsors__image" alt="Pingdom" src="/static/images/sponsors/white/pingdom.07446398.png">
        <span class="sponsors__name">Pingdom</span>
        <span class="sponsors__service">Monitoring</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://cloud.google.com/">
        <img class="sponsors__image" alt="Google" src="/static/images/sponsors/white/google.2f72f26f.png">
        <span class="sponsors__name">Google</span>
        <span class="sponsors__service">BigQuery</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://getsentry.com/for/python">
        <img class="sponsors__image" alt="Sentry" src="/static/images/sponsors/white/sentry.5ab437bc.png">
        <span class="sponsors__name">Sentry</span>
        <span class="sponsors__service">Error logging</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://aws.amazon.com/">
        <img class="sponsors__image" alt="AWS" src="/static/images/sponsors/white/aws.5f800271.png">
        <span class="sponsors__name">AWS</span>
        <span class="sponsors__service">Cloud computing</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.datadoghq.com/">
        <img class="sponsors__image" alt="DataDog" src="/static/images/sponsors/white/datadog.e569d741.png">
        <span class="sponsors__name">DataDog</span>
        <span class="sponsors__service">Monitoring</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.fastly.com/">
        <img class="sponsors__image" alt="Fastly" src="/static/images/sponsors/white/fastly.0563c6f5.png">
        <span class="sponsors__name">Fastly</span>
        <span class="sponsors__service">CDN</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.digicert.com/">
        <img class="sponsors__image" alt="DigiCert" src="/static/images/sponsors/white/digicert.79748718.png">
        <span class="sponsors__name">DigiCert</span>
        <span class="sponsors__service">EV certificate</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://statuspage.io">
        <img class="sponsors__image" alt="StatusPage" src="/static/images/sponsors/white/statuspage.67af0b3d.png">
        <span class="sponsors__name">StatusPage</span>
        <span class="sponsors__service">Status page</span>
      </a>
    
  
</div>

    
  </body>

</html>
"""

base3 = """







<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">

    <meta name="defaultLanguage" content="en">
    <meta name="availableLanguages" content="en">

    

    <title>Register · PyPI</title>
    <meta name="description" content="The Python Package Index (PyPI) is a repository of software for the Python programming language.">

    <link rel="stylesheet" href="/static/css/warehouse.a1809af1.css">
    <link rel="stylesheet" href="/static/css/fontawesome.4b73fd92.css">
    <link rel="stylesheet" href="/static/css/regular.19624371.css">
    <link rel="stylesheet" href="/static/css/solid.f478cfb1.css">
    <link rel="stylesheet" href="/static/css/brands.1ea560bf.css">
    <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Source+Sans+Pro:400,400italic,600,600italic,700,700italic|Source+Code+Pro:500">
    <noscript>
      <link rel="stylesheet" href="/static/css/noscript.ea8974d1.css">
    </noscript>

    

    <link rel="icon" href="/static/images/favicon.6a76275d.ico" type="image/x-icon">

    <link rel="alternate" type="application/rss+xml" title="RSS: 40 latest updates" href="/rss/updates.xml">
    <link rel="alternate" type="application/rss+xml" title="RSS: 40 newest packages" href="/rss/packages.xml">
    

    <meta property="og:url" content="https://pypi.org/account/register/">
    <meta property="og:site_name" content="PyPI">
    <meta property="og:type" content="website">
    <meta property="og:image" content="https://pypi.org/static/images/twitter.c0030826.jpg">
    <meta property="og:title" content="Register">
    <meta property="og:description" content="The Python Package Index (PyPI) is a repository of software for the Python programming language.">

    <link rel="search" type="application/opensearchdescription+xml" title="PyPI" href="/opensearch.xml">

    
    <script
      src="https://cdn.ravenjs.com/3.26.2/raven.min.js"
      integrity="sha384-D6LXy67EIC102DTuqypxwQsTHgiatlbvg7q/1YAWFb6lRyZ1lIZ6bGDsX7jxHNKA"
      crossorigin="anonymous">
    </script>
    
    <script async
            data-ga-id="UA-55961911-1"
            data-sentry-frontend-dsn="https://3a67b35c9dc248a191d761410b095861@sentry.io/1231155"
            src="/static/js/warehouse.b56a7115.js">
    </script>
    
  <script async
  src="/static/js/vendor/zxcvbn.9cf6916d.js">
</script>

    <script async src="https://www.googletagmanager.com/gtag/js?id=UA-55961911-1"></script>
    <script defer src="https://www.fastly-insights.com/insights.js?k=6a52360a-f306-421e-8ed5-7417d0d4a4e9&dnt=true"></script>
  </head>

  <body data-controller="viewport-toggle">
    

    <!-- Accessibility: this link should always be the first piece of content inside the body-->
    <a href="#content" class="skip-to-content">Skip to main content</a>

    <button class="button button--primary button--switch-to-mobile hidden" data-target="viewport-toggle.switchToMobile" data-action="viewport-toggle#switchToMobile">
      Switch to mobile version
    </button>

    <section id="sticky-notifications" class="stick-to-top js-stick-to-top">
      <!-- Add browser warning. Will show for ie9 and below -->
      <!--[if IE]>
      <div class="notification-bar notification-bar--danger">
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning:</span>
        </span>
        <span class="notification-bar__message">You are using an unsupported browser, upgrade to a newer version.</span>
      </div>
      <![endif]-->
      
      <noscript>
      <div class="notification-bar notification-bar--danger">
        
        <span class="notification-bar__icon">
          <i class="fa fa-exclamation-triangle" aria-hidden="true"></i>
          <span class="sr-only">Warning:</span>
        </span>
        <span class="notification-bar__message">Some features may not work without JavaScript. Please try enabling it if you encounter problems.</span>
      </div>
      </noscript>
    </section>

    
      <div data-html-include="/_includes/flash-messages/">
      </div>
    

    

    

    <header class="site-header ">
      <div class="site-container">
        <div class="split-layout">
          
          <div class="split-layout">
            <div>
              <a class="site-header__logo" href="/">
                <img alt="PyPI" src="/static/images/logo-small.6eef541e.svg">
              </a>
            </div>

            <form class="search-form search-form--primary" action="/search/">
              <div role="search">
                <label for="search" class="sr-only">Search PyPI</label>
                <input id="search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="">
                
                <button type="submit" class="search-form__button">
                  <i class="fa fa-search" aria-hidden="true"></i>
                  <span class="sr-only">Search</span>
                </button>
              </div>
            </form>
          </div>
          

          <div data-html-include="/_includes/current-user-indicator/">
            <nav id="user-indicator" class="horizontal-menu horizontal-menu--light horizontal-menu--tall" aria-label="Main navigation">
  <a class="horizontal-menu__link horizontal-menu__link--remove-on-mobile" href="/help/">Help</a>
  <a class="horizontal-menu__link horizontal-menu__link--remove-on-mobile" href="https://donate.pypi.org">Donate</a>
  <a class="horizontal-menu__link" href="/account/login/">Log in</a>
  <a class="horizontal-menu__link" href="/account/register/">Register</a>
</nav>
          </div>
        </div>
      </div>
    </header>

    
    <section class="mobile-search">
      <form class="search-form search-form--fullwidth" action="/search/">
        <div role="search">
          <label for="mobile-search" class="sr-only">Search PyPI</label>
          <input id="mobile-search" class="search-form__search" type="text" name="q" placeholder="Search projects" value="">
          
          <button type="submit" class="search-form__button">
            <i class="fa fa-search" aria-hidden="true"></i>
            <span class="sr-only">Search</span>
          </button>
          </button>
        </div>
      </form>
    </section>
    

    <main id="content">
      
  
    
  

  <section class="horizontal-section">
    <div class="site-container">
      <h1 class="page-title">Create an account on PyPI</h1>

      <form method="POST" action="/account/register/" data-controller="password password-match password-strength-gauge">
        <input name="csrf_token" type="hidden" value="tS0Gwq1bJZfFQCf-A9vfS5-fzGoVKJ81fN-lAM2xsW4">

        

        <div class="form-group">
          <label for="full_name" class="form-group__label">Name</label>
          <input autofocus class="form-group__input" id="full_name" name="full_name" placeholder="Your name" required="required" tabindex="1" type="text" value="">
          
        </div>

        <div class="form-group">
          <label for="full_name" class="form-group__label">Email address</label>
          <input autocomplete="email" class="form-group__input" id="email" name="email" placeholder="Your email address" required="required" tabindex="2" type="email" value="">
          
        </div>

        
        <div class="form-group confirm-form">
          <label for="confirm_form" class="form-group__label">Confirm form</label>
          <input aria-hidden="true" class="form-group__input" id="confirm_form" name="confirm_form" type="text" value="">
        </div>

        <div class="form-group">
          <label for="username" class="form-group__label">Username</label>
          <input autocapitalize="off" autocomplete="username" autocorrect="off" class="form-group__input" id="username" name="username" placeholder="Select a username" required="required" spellcheck="false" tabindex="3" type="text" value="">
          
        </div>

        <div>
          <div class="form-group">
            <div class="split-layout">
              <label for="password" class="form-group__label">Password</label>
              <label for="show-password">
                <input data-action="change->password#togglePasswords" data-target="password.showPassword"
                  id="show-password" type="checkbox" tabindex="7">&nbsp;Show passwords
              </label>
            </div>
            
            <div>
              <input autocomplete="new-password" class="form-group__input" data-action="keyup-&gt;password-match#checkPasswordsMatch keyup-&gt;password-strength-gauge#checkPasswordStrength" data-target="password.password password-match.passwordMatch password-strength-gauge.password" id="new_password" name="new_password" placeholder="Select a password" required="required" tabindex="4" type="password" value="">
            </div>
            
            <p class="form-group__help-text">
  Choose a strong password that contains letters (uppercase and lowercase), numbers and special characters. Avoid common words or repetition.
</p>
<p class="form-group__help-text">
  <strong>Password strength:</strong>
  <span class="password-strength">
    <span class="password-strength__gauge" data-target="password-strength-gauge.strengthGauge">
      <span class="sr-only">Password field is empty</span>
    </span>
  </span>
</p>
          </div>

          <div class="form-group">
            <label for="password_confirm" class="form-group__label">Confirm password</label>
            <input class="form-group__input" data-action="keyup-&gt;password-match#checkPasswordsMatch" data-target="password.password password-match.passwordMatch" id="password_confirm" name="password_confirm" placeholder="Confirm password" required="required" tabindex="5" type="password" value="">
            
          </div>
        </div>

        <div class="form-group">
          <ul class="form-errors">
            <li data-target="password-match.matchMessage" class="hidden"></li>
          </ul>
        </div>

        <input type="submit" value="Create account" class="button button--primary" data-target="password-match.submit" tabindex="6">
      </form>
    </div>
  </section>

    </main>

    <footer class="footer" role="contentinfo">
      <div class="footer__logo">
        <img src="/static/images/white-cube.8c3a6fe9.svg" alt="Logo" class="-js-white-cube">
      </div>

      <div class="footer__menus">
        <ul class="footer__menu">
          <li>
            <h2>Help</h2>
          </li>
          <li><a href="https://packaging.python.org/installing/">Installing packages</a></li>
          <li><a href="https://packaging.python.org/distributing/">Uploading packages</a></li>
          <li><a href="https://packaging.python.org/">User guide</a></li>
          <li><a href="/help/">FAQs</a></li>
        </ul>
        <ul class="footer__menu">
          <li>
            <h2>About PyPI</h2>
          </li>
          
          <li><a href="https://status.python.org/">Status: <span data-statuspage-domain="https://2p66nmmycsj3.statuspage.io">all systems operational</span></a></li>
          
          <li><a href="https://dtdg.co/pypi">Infrastructure dashboard</a></li>
          <li><a href="https://www.python.org/dev/peps/pep-0541/">Package index name retention</a></li>
          <li><a href="/sponsors/">Our sponsors</a></li>
        </ul>


        <ul class="footer__menu">
          <li>
            <h2>Contributing to PyPI</h2>
          </li>
          <li><a href="/help/#feedback">Bugs and feedback</a></li>
          <li><a href="https://github.com/pypa/warehouse">Contribute on GitHub</a></li>
          <li><a href="https://github.com/pypa/warehouse/graphs/contributors">Development credits</a></li>
        </ul>
        <ul class="footer__menu">
          <li>
            <h2>Using PyPI</h2>
          </li>
          <li><a href="https://www.pypa.io/en/latest/code-of-conduct/">Code of conduct</a></li>
          <li><a href="/security/">Report security issue</a></li>
          <li><a href="https://www.python.org/privacy/">Privacy policy</a></li>
          <li><a href="/policy/terms-of-use/">Terms of use</a></li>
        </ul>
      </div>

      <hr class="footer__divider">

      <div class="footer__text">
        <p>
          Developed and maintained by the Python community, for the Python community.
          <br>
          <a href="https://donate.pypi.org">Donate today!</a>
        </p>
        <p>© 2018 <a href="https://www.python.org/psf/">Python Software Foundation</a></p>
      </div>

      <div class="centered hide-on-desktop">
        <button class="button button--switch-to-desktop hidden" data-target="viewport-toggle.switchToDesktop" data-action="viewport-toggle#switchToDesktop">
          Desktop version
        </button>
      </div>
    </footer>

    

<div class="sponsors">
  <p class="sponsors__title">Supported by</p>
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.elastic.co/">
        <img class="sponsors__image" alt="Elastic" src="/static/images/sponsors/white/elastic.a912fb87.png">
        <span class="sponsors__name">Elastic</span>
        <span class="sponsors__service">Search</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.pingdom.com/">
        <img class="sponsors__image" alt="Pingdom" src="/static/images/sponsors/white/pingdom.07446398.png">
        <span class="sponsors__name">Pingdom</span>
        <span class="sponsors__service">Monitoring</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://cloud.google.com/">
        <img class="sponsors__image" alt="Google" src="/static/images/sponsors/white/google.2f72f26f.png">
        <span class="sponsors__name">Google</span>
        <span class="sponsors__service">BigQuery</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://getsentry.com/for/python">
        <img class="sponsors__image" alt="Sentry" src="/static/images/sponsors/white/sentry.5ab437bc.png">
        <span class="sponsors__name">Sentry</span>
        <span class="sponsors__service">Error logging</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://aws.amazon.com/">
        <img class="sponsors__image" alt="AWS" src="/static/images/sponsors/white/aws.5f800271.png">
        <span class="sponsors__name">AWS</span>
        <span class="sponsors__service">Cloud computing</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.datadoghq.com/">
        <img class="sponsors__image" alt="DataDog" src="/static/images/sponsors/white/datadog.e569d741.png">
        <span class="sponsors__name">DataDog</span>
        <span class="sponsors__service">Monitoring</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.fastly.com/">
        <img class="sponsors__image" alt="Fastly" src="/static/images/sponsors/white/fastly.0563c6f5.png">
        <span class="sponsors__name">Fastly</span>
        <span class="sponsors__service">CDN</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://www.digicert.com/">
        <img class="sponsors__image" alt="DigiCert" src="/static/images/sponsors/white/digicert.79748718.png">
        <span class="sponsors__name">DigiCert</span>
        <span class="sponsors__service">EV certificate</span>
      </a>
    
  
    
      <a class="sponsors__sponsor" target="_blank" rel="noopener" href="https://statuspage.io">
        <img class="sponsors__image" alt="StatusPage" src="/static/images/sponsors/white/statuspage.67af0b3d.png">
        <span class="sponsors__name">StatusPage</span>
        <span class="sponsors__service">Status page</span>

"""


class PageHunterTestCase(unittest.TestCase):

    def test_testpage(self):
        """"""
        hunter = core.PageHunter(base1)
        hunter.add_base_page_string(base2)

        self.assertTrue(hunter.pass_stable_checking)
        self.assertTrue(hunter._noscript_stable)
        self.assertTrue(hunter._raw_stable)
        self.assertTrue(hunter._text_stable)

        self.assertFalse(hunter.dynamic_raw)
        self.assertFalse(hunter.dynamic_noscript)
        self.assertFalse(hunter.dynamic_text)
        self.assertFalse(hunter.heavy_dynamic_noscript)
        self.assertFalse(hunter.heavy_dynamic_raw)
        self.assertFalse(hunter.heavy_dynamic_text)

        hunter.add_base_page_string(base3)
        self.assertTrue(hunter.pass_stable_checking)
        print(core.Page(base3).without_script_and_style)
        print(core.Page(base1).without_script_and_style)
        self.assertFalse(hunter._noscript_stable)
        self.assertFalse(hunter._raw_stable)
        self.assertTrue(hunter._text_stable)
        self.assertTrue(hunter.dynamic_raw)
        self.assertTrue(hunter.dynamic_noscript)
        self.assertFalse(hunter.dynamic_text)
        self.assertFalse(hunter.heavy_dynamic_noscript)
        self.assertFalse(hunter.heavy_dynamic_raw)
        self.assertFalse(hunter.heavy_dynamic_text)

        print(hunter.calc_ratio_with_base_page(core.Page(base3)))


if __name__ == '__main__':
    unittest.main()
