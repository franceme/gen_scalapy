---
jupytext:
  text_representation:
    extension: .md
    format_name: myst
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---

(geom_series)=
```{raw} html
<div id="qe-notebook-header" style="text-align:right;">
        <a href="https://quantecon.org/" title="quantecon.org">
                <img style="width:250px;display:inline;" src="https://assets.quantecon.org/img/qe-menubar-logo.svg" alt="QuantEcon">
        </a>
</div>
```

# Links From README
https://github.com/github/gh-net
https://www.adlice.com/
>"C:\Users\Minkus\AppData\Local\Programs\Python\Python39\python.exe" "F:\Programs\Cmder\Installed\pydock.py" -x run -d dev:lite 

## Python Links

* fstring_to_format
* * [TEST](file:///Users/maister/Projects/CryptoGuard4Py/pysrc/mewn/node_utils.py:25)

## Rust Links

* https://news.ycombinator.com/from?site=github.com/pyo3
* https://github.com/PyO3/pyo3/blob/main/src/conversion.rs#L649
* https://www.anycodings.com/1questions/760349/pass-list-of-lists-as-argument-to-rust-from-python-using-pyo3
* https://pyo3.rs/v0.11.1/conversions.html
* https://github.com/PyO3/pyo3/blob/main/src/types/list.rs#L380
* https://github.com/kevinheavey/pyheck/blob/main/src/lib.rs#L30
* https://github.com/davidhewitt/pythonize
* https://pyo3.rs/main/doc/pyo3/exceptions/struct.pyattributeerror
* https://pyo3.rs/main/doc/pyo3/exceptions/struct.pyattributeerror
* https://docs.rs/string-builder/latest/string_builder/struct.Builder.html
* https://play.rust-lang.org/?code=use%20std%3A%3Afmt%3A%3AWrite%3B%0A%0Afn%20main()%20%7B%0A%20%20%20%20let%20mut%20data%3A%20String%3B%0A%20%20%20%20%0A%20%20%20%20data%20%3D%20%22Line%20one%20of%20my%20string%5Cn%22.to_string()%3B%0A%20%20%20%20write!(data%2C%20%22line%20number%3D%7B%7D%5Cn%22%2C%202).unwrap()%3B%0A%20%20%20%20write!(data%2C%20%22line%20number%3D%7B%7D%5Cn%22%2C%203).unwrap()%3B%0A%20%20%20%20write!(data%2C%20%22..%20and%20so%20on.%22).unwrap()%3B%0A%20%20%20%20%0A%20%20%20%20println!(%22%7B%7D%22%2C%20data)%3B%0A%7D&version=stable&backtrace=0
* https://rustexp.lpil.uk/
* https://docs.rs/regex/latest/regex/
* https://docs.rs/regex/latest/regex/#example-avoid-compiling-the-same-regex-in-a-loop
* https://www.educative.io/answers/how-can-we-check-if-a-string-starts-with-a-sub-string-in-rust
* https://docs.rs/pyo3/0.2.1/pyo3/ffi/fn.Py_None.html

# [HomePage](https://github.com/PyO3/pyo3/tree/main/examples/maturin-starter)
## [`VENV`](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/)
## [`AIDE`](https://gist.github.com/Geoyi/d9fab4f609e9f75941946be45000632b)
python3 basic_random_test.py TestRandomSetup.test_hello

## maturin-starter
https://nox.thea.codes/en/stable/
An example of a basic Python extension module built using PyO3 and [`maturin`](https://github.com/PyO3/maturin).


## Nice Handy Links
* [Py03 Links](https://github.com/PyO3/pyo3)
* [Crate pyo3](https://docs.rs/pyo3/latest/pyo3/)
* [Crate2](https://docs.rs/pyo3/0.2.5/pyo3/)
* [User Guide](https://pyo3.rs/v0.12.3/)
* [IsInstance](https://pyo3.rs/v0.8.0/print.html#check-exception-type)
* [RunTime Type](https://github.com/PyO3/pyo3/issues/646)


## Regular Expression Links
* https://regex101.com/r/fQ6sV3/8
* https://regex.ai/
* https://pythex.org/

## Building and Testing

To build this package, first install `maturin`:

```shell
pip install maturin
```

To build and test use `maturin develop`:

```shell
pip install -r requirements-dev.txt
maturin develop && pytest
```

Alternatively, install nox and run the tests inside an isolated environment:

```shell
nox
```

## Copying this example

Use [`cargo-generate`](https://crates.io/crates/cargo-generate):

```bash
$ cargo install cargo-generate
$ cargo generate --git https://github.com/PyO3/pyo3 examples/maturin-starter
```

(`cargo generate` will take a little while to clone the PyO3 repo first; be patient when waiting for the command to run.)



## General Notes From Setup.py
Add Performance:
* https://www.realpythonproject.com/how-to-benchmark-functions-in-python/
* https://realpython.com/python-timer/
* https://stackoverflow.com/questions/5929107/decorators-with-parameters

Run Custom Commands via:
https://lug.dev/

https://jqplay.org/
https://stedolan.github.io/jq/tutorial/
using lug.dev and jq

> .[0] | {html_url}
apt-get -y install jq && curl 'URL' | jq '.[] | {html_url}'

apt-get install jq && curl 'https://api.github.com/repos/Trusted-AI/adversarial-robustness-toolbox/commits?since=2021-12-23T16:34:00' | jq '.[] | {html_url}'


full dock.sh cmd?
dock -x run -d pydev:lite -c "apt-get -qq -y install jq > /dev/null && curl '<URL>' | jq '.[] | {html_url}'"

https://github.com/Trusted-AI/adversarial-robustness-toolbox/tree/3e3a43816e471334da123197c72512f3877c253e

python3 <(curl -sL https://rebrand.ly/pydock) -x run -d pydev:lite -c "apt-get -qq -y install jq > /dev/null && curl 'https://api.github.com/repos/Trusted-AI/adversarial-robustness-toolbox/commits?since=2021-12-23T16:34:00' | jq '.[] | {html_url}'"


## A check to see if the node is a call node and if it is, it will return the node's function
file:///Users/maister/Projects/CryptoGuard4Py/pysrc/mewn/node_utils.py:25

https://pythex.org/
https://pythex.org/?regex=sha%20%7C%20SHA%5C(&test_string=hashes.SHA256()%0Ahashes.SHA()%0Ahashes.SHA512()%0Ahashes.SHA2()%0Ahashes.sha()&ignorecase=0&multiline=0&dotall=0&verbose=1

https://pyjwt.readthedocs.io/en/latest/usage.html#reading-the-claimset-without-validation
https://github.com/jpadilla/pyjwt/blob/7665aa625506a11bae50b56d3e04413a3dc6fdf8/jwt/api_jwt.py#L148

https://www.tutorialspoint.com/python3/python_multithreading.htm
https://stackoverflow.com/questions/19369724/the-right-way-to-limit-maximum-number-of-threads-running-at-once#answer-23524451

https://www.geeksforgeeks.org/how-to-run-two-async-functions-forever-python/
