# Finding the Sum of the Series ∑(1/n²) Using Parseval's Theorem

**Hello everyone!**

Today, I'm going to walk you through a fascinating problem: finding the exact value of the infinite series:

\[
\sum_{n=1}^{\infty} \frac{1}{n^2}
\]

Using **Parseval's theorem** and Fourier series, we'll arrive at the well-known result:

\[
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
\]

Let's dive in step by step.

---

## **Step 1: Understanding Parseval's Theorem**

First, let's recall **Parseval's theorem** for Fourier series. For a function \( f(x) \) defined on the interval \([-L, L]\) with Fourier coefficients \( a_n \) and \( b_n \), Parseval's theorem states:

\[
\frac{1}{L} \int_{-L}^{L} |f(x)|^2 \, dx = \frac{a_0^2}{2} + \sum_{n=1}^{\infty} \left( a_n^2 + b_n^2 \right)
\]

**Key Insight:** This theorem connects the integral of the square of a function over an interval to the sum of the squares of its Fourier coefficients. By choosing an appropriate function, we can relate the series we're interested in to these coefficients.

---

## **Step 2: Choosing the Appropriate Function**

I need a function whose Fourier coefficients involve \( \frac{1}{n} \) or \( \frac{1}{n^2} \). A classic choice is:

\[
f(x) = x
\]

defined on \( (-\pi, \pi) \), extended periodically. Since \( x \) is an odd function, its Fourier series will contain only sine terms.

**Key Insight:** Choosing \( f(x) = x \) simplifies the problem because it eliminates cosine terms and \( a_n \) coefficients, focusing our attention on \( b_n \).

---

## **Step 3: Computing the Fourier Coefficients**

For \( f(x) = x \), the Fourier coefficients are:

- \( a_0 = 0 \) (since \( x \) is odd)
- \( a_n = 0 \) (cosine terms vanish)
- \( b_n = \frac{1}{\pi} \int_{-\pi}^{\pi} x \sin(nx) \, dx \)

Simplify \( b_n \):

Since \( x \sin(nx) \) is even, we can write:

\[
b_n = \frac{2}{\pi} \int_{0}^{\pi} x \sin(nx) \, dx
\]

Now, I'll integrate by parts:

- Let \( u = x \), \( dv = \sin(nx) \, dx \)
- Then \( du = dx \), \( v = -\frac{\cos(nx)}{n} \)

Applying integration by parts:

\[
b_n = \frac{2}{\pi} \left( -\frac{x \cos(nx)}{n} \Big|_{0}^{\pi} + \frac{1}{n} \int_{0}^{\pi} \cos(nx) \, dx \right)
\]

Compute the boundary term:

\[
-\frac{x \cos(nx)}{n} \Big|_{0}^{\pi} = -\frac{\pi \cos(n\pi)}{n} + 0 = -\frac{\pi (-1)^n}{n}
\]

Compute the integral:

\[
\frac{1}{n} \int_{0}^{\pi} \cos(nx) \, dx = \frac{1}{n} \left[ \frac{\sin(nx)}{n} \Big|_{0}^{\pi} \right] = 0
\]

So, \( b_n \) simplifies to:

\[
b_n = \frac{2}{\pi} \left( -\left( -\frac{\pi (-1)^n}{n} \right) \right) = \frac{2 (-1)^n}{n}
\]

**Key Insight:** The calculation of \( b_n \) yields coefficients inversely proportional to \( n \), which will lead to \( \frac{1}{n^2} \) when squared in Parseval's theorem.

---

## **Step 4: Applying Parseval's Theorem**

Since \( a_0 = a_n = 0 \), Parseval's theorem reduces to:

\[
\frac{1}{\pi} \int_{-\pi}^{\pi} |f(x)|^2 \, dx = \sum_{n=1}^{\infty} b_n^2
\]

Substitute \( b_n \):

\[
\sum_{n=1}^{\infty} b_n^2 = \sum_{n=1}^{\infty} \left( \frac{2 (-1)^n}{n} \right)^2 = 4 \sum_{n=1}^{\infty} \frac{1}{n^2}
\]

Compute the integral on the left:

\[
\frac{1}{\pi} \int_{-\pi}^{\pi} x^2 \, dx = \frac{2}{\pi} \int_{0}^{\pi} x^2 \, dx
\]

Calculating the integral:

\[
\int_{0}^{\pi} x^2 \, dx = \left. \frac{x^3}{3} \right|_{0}^{\pi} = \frac{\pi^3}{3}
\]

So,

\[
\frac{2}{\pi} \cdot \frac{\pi^3}{3} = \frac{2 \pi^2}{3}
\]

Thus, Parseval's theorem gives:

\[
\frac{2 \pi^2}{3} = 4 \sum_{n=1}^{\infty} \frac{1}{n^2}
\]

**Key Insight:** We now have an equation that directly relates the series we're interested in to a known integral value.

---

## **Step 5: Solving for the Sum**

Divide both sides by 4:

\[
\frac{2 \pi^2}{3 \times 4} = \sum_{n=1}^{\infty} \frac{1}{n^2}
\]

Simplify:

\[
\frac{\pi^2}{6} = \sum_{n=1}^{\infty} \frac{1}{n^2}
\]

**Key Insight:** This final step isolates the sum, revealing its exact value in terms of \( \pi \).

---

## **Conclusion**

By applying Parseval's theorem to the function \( f(x) = x \), we have shown that:

\[
\sum_{n=1}^{\infty} \frac{1}{n^2} = \frac{\pi^2}{6}
\]

This is a remarkable result connecting an infinite series to the fundamental constant \( \pi \). It showcases the power of Fourier analysis in solving problems in mathematical analysis.

---

## **Final Thoughts**

This method not only provides the value of the series but also highlights the deep connections between different areas of mathematics—specifically, how Fourier series and Parseval's theorem can solve problems in number theory and series summation.

Thank you for joining me in this exploration!
