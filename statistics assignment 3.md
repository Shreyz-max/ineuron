
# Problem Statement 1:

Blood glucose levels for obese patients have a mean of 100 with a standard deviation of 15. A researcher thinks that a diet high in raw cornstarch will have a positive effect on
blood glucose levels. A sample of 36 patients who have tried the raw cornstarch diet
have a mean glucose level of 108. Test the hypothesis that the raw cornstarch had an
effect or not.

$\underline{Hypothesis:}$

<li>$ \text{Null Hypothesis } H_{0} : \mu = 100 $

<li>$ \text{Alternate Hypothesis }H_{A} : \mu > 100 $

$\text{We will use z−test as the sample is large with a known population variance.}$

$\underline{Parameters:}$

<li>$ \mu = 100$

<li>$ \sigma = 15$ 

<li>$ \bar{x} = 108$

<li>$ n = 36 $

$\underline{Significance}$

$ \alpha = 0.05$

$\text{Formula for test statistic is: }$
$\begin{equation}
z = \frac{\bar{x} − \mu}{\frac{\sigma}{\sqrt{n}}}\end{equation}$

$\begin{equation}
z = \frac{108 − 100}{\frac{15}{\sqrt{36}}}
= 3.2\end{equation}$

$\text{For a significance of 0.05 the critical value is 1.645 for a right−tailed test.}$

$\text{Since 1.645 < 3.2 we will reject the null hypothesis }H_{0} \text{ in favour of alternate hypothesis }H_{A}.$

<h3>Conclusion:</h3> 
<p style='font-size:120%'>Since the null hypothesis is rejected at a significant level of 5%, we can conclude that raw starch had effect on blood glucose levels.</p>

# Problem Statement 2:

In one state, 52% of the voters are Republicans, and 48% are Democrats. In a second
state, 47% of the voters are Republicans, and 53% are Democrats. Suppose a simple
random sample of 100 voters are surveyed from each state.

What is the probability that the survey will show a greater percentage of Republican
voters in the second state than in the first state?

$\underline{Parameters:}$

<li>$ P_{1} \text{ proportion of republicans in first state= 0.52}$

<li>$ P_{2} \text{ proportion of republicans in second state= 0.47}$

<li>$ p_{1} \text{ is sample proportion of republicans in first state}$

<li>$ p_{2} \text{ is sample proportion of republicans in second state}$

<li>$ \text{Mean sample differnce = 0.52 − 0.47 = 0.05}$ 

<li>$ \sigma = \sqrt{\frac{P_{1}(1 − P_{1} )}{n_{1}} + \frac{P_{2}(1 − P_{2} )}{n_{2}}} = \sqrt{\frac{0.52(1 − 0.52)}{100} + \frac{0.47(1 − 0.47)}{100}} = 0.0706$

$\text{We need to find probability where }p_{1} − p_{2} < 0$

$\text{z−score is:}$

$\begin{equation}\frac{x − \mu_{p_{1} − p_{2}}}{\sigma} = \frac{0 − 0.05}{0.0706} = -0.7082\end{equation}$
 
$\text{Using tables we fine the probability for z−score -0.7082 is 0.24}$

# Problem Statement 3:

You take the SAT and score 1100. The mean score for the SAT is 1026 and the standard
deviation is 209. How well did you score on the test compared to the average test taker?

$\underline{Parameters:}$

<li>$ \mu = 1026$

<li>$ \sigma = 209$ 

<li>$ \bar{x} = 1100$

$\text{z−score for my score is }$

$\begin{equation}z = \frac{1100 − 1026}{209}
= 0.354\end{equation}$

$\text{Using the tables, the probability for my z−score is 0.638.}$

<h3>Conclusion:</h3> 
<p style="font-size:120%">With a score of 1100, I am better than 63.8% of the  people who took the test. An average test taker has 50%, so I am better by 13.8%.</p>
