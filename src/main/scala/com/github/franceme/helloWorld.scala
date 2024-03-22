package com.github.franceme

import com.sun.jna.Native
import me.shadaj.scalapy.py
import py.PyQuote

import scala.collection.mutable
import scala.util.{Failure, Success}

import me.shadaj.scalapy.py
import me.shadaj.scalapy.py.SeqConverters

object helloWorld extends App {
    println("Hello World")

    val listLengthPython = py.Dynamic.global.len(List(1, 2, 3, 4, 5).toPythonProxy)

    println(listLengthPython)
}
