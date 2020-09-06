===
sho
===


.. image:: https://img.shields.io/pypi/v/sho.svg
        :target: https://pypi.python.org/pypi/sho

.. image:: https://img.shields.io/travis/davewd/sho.svg
        :target: https://travis-ci.org/davewd/sho

.. image:: https://readthedocs.org/projects/sho/badge/?version=latest
        :target: https://sho.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://readthedocs.org/projects/sho/badge/?version=latest
        :target: https://sho.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: https://pyup.io/repos/github/davewd/sho/shield.svg
     :target: https://pyup.io/repos/github/davewd/sho/
     :alt: Updates

.. image:: https://img.shields.io/pypi/dm/sho
     :target: https://pypistats.org/packages/sho
     :alt: PyPI - Downloads


What is sho?
-------------------
**Sho is a one line python command to "sho.w()" any variable for easy exploration**

    import sho
    
    sho.w(dataframe)

Which datatypes are currently handled ?
---------------------------------------
+------------------+---------------+-------------+
| Datatype         | Visualization | Implemented |
+==================+===============+=============+
| pandas.DataFrame | pivottablejs_ | Yes         |
+------------------+---------------+-------------+

.. _pivottablejs: https://pivottable.js.org

Development
-----------

* to test the unit tests run : python -m unittest test.test_sho

Credits
-------

:Authors:
    davewd_

:Version: 1.0 of 2020/08/26
:Dedication: To my family.
:License: "Free software: MIT license"
:Documentation: https://sho.readthedocs.io.

.. _davewd: http://www.github.com/davewd

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
