<html>

<h1>Hello There</h1>

<p>This is an example of a pml file</p>

<pml>
    def f():
        b = 2
        if b > 2:
            return "<h2>Say Hello!</h2>"
        elif b < 3:
            return "<h2>Say NonnyNo!</h2>"
    pml = f()
</pml>


<h2>Don't Go!</h2>

<pml>
    def g():
        return "<h3>Now, Good Bye...!</h3>"
    pml = g()
</pml>

</html>
