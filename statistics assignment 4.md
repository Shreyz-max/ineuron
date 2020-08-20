
# Problem Statement 1:

Is gender independent of education level? A random sample of 395 people were
surveyed and each person was asked to report the highest education level they
obtained. The data that resulted from the survey is summarized in the following table:

<table style="width:40%">
  <tr>
    <th></th>
    <th>High School</th>
    <th>Bachelors</th>
    <th>Masters</th>
    <th>Ph.d.</th>
    <th>Total</th>
  </tr>
  <tr>
    <th>Female</th>
    <td>60</td>
    <td>54</td>
    <td>46</td>
    <td>41</td>
    <td>201</td>
  </tr>
  <tr>
    <th>Male</th>
    <td>40</td>
    <td>44</td>
    <td>53</td>
    <td>57</td>
    <td>194</td>
  </tr>
  <tr>
      <th>Total</th>
      <td>100</td>
      <td>98</td>
      <td>99</td>
      <td>98</td>
      <td>395</td>
  </tr>
 </table>
 

Question: Are gender and education level dependent at 5% level of significance? In
other words, given the data collected above, is there a relationship between the
gender of an individual and the level of education that they have obtained?

$\underline{Hypothesis:}$

<li>$ \text{Null Hypothesis } H_{0} \text{ gender and education are independent of each other.}$

<li>$ \text{Alternate Hypothesis }H_{A} \text{ education is dependent on gender.}$

$\underline{Parameters}$

<li>$\text{Degrees of freedom is (r − 1)(c − 1) = (2 − 1)(4 − 1) = 3}$

$\underline{Significance}$

<li>$ \alpha = 0.05$


<table style="width:70%">
<caption style="text-align:center">Observed Counts</caption>
  <tr>
    <th></th>
    <th>High School</th>
    <th>Bachelors</th>
    <th>Masters</th>
    <th>Ph.d.</th>
    <th>Total</th>
  </tr>
  <tr>
    <th>Female</th>
    <td>60</td>
    <td>54</td>
    <td>46</td>
    <td>41</td>
    <td>201</td>
  </tr>
  <tr>
    <th>Male</th>
    <td>40</td>
    <td>44</td>
    <td>53</td>
    <td>57</td>
    <td>194</td>
  </tr>
  <tr>
      <th>Total</th>
      <td>100</td>
      <td>98</td>
      <td>99</td>
      <td>98</td>
      <td>395</td>
  </tr>
 </table>

$\text{Probability that a person completed high school P(HS): }\frac{100}{395} \text{= 0.253}$

\text{Probability that a person completed Bachelors P(B): }\frac{98}{395} \text{= 0.248}$

\text{Probability that a person completed Masters P(M): }\frac{99}{395} \text{= 0.251}$

\text{Probability that a person completed PhD P(P): }\frac{98}{395} \text{= 0.248}$

<table style="width:70%">
<caption style="text-align:center">Expected Counts</caption>
  <tr>
    <th></th>
    <th>High School</th>
    <th>Bachelors</th>
    <th>Masters</th>
    <th>Ph.d.</th>
  </tr>
  <tr>
    <th>Female</th>
    <td>P(HS) * 201 = <b>50.853</b></td>
    <td>P(B) * 201 = <b>49.848</b></td>
    <td>P(M) * 201 = <b>50.451</b></td>
    <td>P(P) * 201 = <b>49.848</b></td>
  </tr>
  <tr>
    <th>Male</th>
    <td>P(HS) * 194 = <b>49.082</b></td>
    <td>P(B) * 194 = <b>48.112</b></td>
    <td>P(M) * 194 = <b>48.694</b></td>
    <td>P(P) * 194 = <b>48.112</b></td>
  </tr>
 </table>



$\chi^{2} = \sum{\frac{(Observed − Expected)^{2}}{Expected}}$

$\begin{equation}\frac{(60 − 50.853)^{2}}{50.853} + \frac{(54 − 49.848)^{2}}{49.848} + \frac{(46 − 50.451)^{2}}{50.451} + \frac{(41 − 49.848)^{2}}{49.848} + \frac{(40 − 49.082)^{2}}{49.082} + \frac{(44 − 48.112)^{2}}{48.112} + \frac{(53 − 48.694)^{2}}{48.694} + \frac{(57 − 48.112)^{2}}{48.112} = 8.006\end{equation}$


$\text{For α = 0.05 and degrees of freedom 3, the critical value is 7.815.}$

$\text{Since 7.815 < 8.006 the value lies in the rejection region. We will reject the null hypothesis }H_{0}.$

<h3>Conclusion:</h3> 
<p style='font-size:120%'>Since the null hypothesis is rejected, we can conclude that for a significance of 5% education depends on gender .</p>

# Problem Statement 2:

Using the following data, perform a oneway analysis of variance using α=.05. Write
up the results in APA format.

[Group1: 51, 45, 33, 45, 67]

[Group2: 23, 43, 23, 43, 45]

[Group3: 56, 76, 74, 87, 56]

$\underline{Hypothesis:}$

<li>$ \text{Null Hypothesis } H_{0}: \quad \mu_{1} = \mu_{2} = \mu_{3}$

<li>$ \text{Alternate Hypothesis }H_{A} \text{ there is atleast one difference among the means.}$

$\underline{Significance}$

<li>$ \alpha = 0.05$

$\underline{Parameters}$

<li>$df_{between} = 3 − 1 = 2$

<li>$df_{within} = 15 − 3 = 12$

<li>$df_{total} = 2 + 12 = 14$

<table style="width:100%">
    <tr>
        <th></th>
        <th>Group 1 (G1)</th>
        <th>Group 2 (G2)</th>
        <th>Group 3 (G3)</th>
        <th>$(G1 − G1_{mean})^{2}$</th>
        <th>$(G2 − G2_{mean})^{2}$</th>
        <th>$(G3 − G3_{mean})^{2}$</th>
    </tr>
    <tr>
        <th></th>
        <td>51</td>
        <td>23</td>
        <td>56</td>
        <td>7.84</td>
        <td>153.76</td>
        <td>190.44</td>
    </tr>
    <tr>
        <th></th>
        <td>45</td>
        <td>43</td>
        <td>76</td>
        <td>10.24</td>
        <td>57.76</td>
        <td>38.44</td>
    </tr>
    <tr>
        <th></th>
        <td>33</td>
        <td>23</td>
        <td>74</td>
        <td>231.04</td>
        <td>153.76</td>
        <td>17.64</td>
    </tr>
    <tr>
        <th></th>
        <td>45</td>
        <td>43</td>
        <td>87</td>
        <td>10.24</td>
        <td>57.76</td>
        <td>295.84</td>
    </tr>
    <tr>
        <th></th>
        <td>67</td>
        <td>45</td>
        <td>56</td>
        <td>353.44</td>
        <td>92.16</td>
        <td>190.44</td>
    </tr>
    <tr>
        <th>Total</th>
        <th>241</th>
        <th>177</th>
        <th>349</th>
        <th>612.8</th>
        <th>515.2</th>
        <th>732.8</th>
    </tr>
    <tr>
        <th>Mean</th>
        <th>48.2</th>
        <th>35.4</th>
        <th>69.8</th>
        <td></td>
        <td></td>
        <td></td>
    </tr>
</table>

$\text{Grand mean (GM) is :} \frac{48.2 + 35.4 + 69.8}{3} = 51.13$

$\begin{equation}SS_{between} = \sum(x_{i} − GM)^{2}*n_{i} = 8.60 * 5 + 247.54 * 5 + 348.44 * 5
 = 3022.95\end{equation}$

$\begin{equation}MSST = \frac{SS_{between}}{df_{between}} = \frac{3022.95}{2} = 1511.47\end{equation}$

$\begin{equation}SS_{within} = \sum(x_{ij} − \bar{x_{j}})^{2} = 612.8 +	515.2 + 732.8 = 1860.8\end{equation}$

$\begin{equation}MSSE = \frac{SS_{within}}{df_{within}} = \frac{1860.8}{12} = 155.07\end{equation}$

$\begin{equation}F−statistics = \frac{MSST}{MSSE} = \frac{1511.47}{155.07} = 9.75\end{equation}$

$\text{At 5% significance and degree of freedom (2, 12) : F-critical = 3.89 }$

$\text{Since 3.89 < 9.75, we will reject the null hypothesis }H_{0}$

<h3>Conclusion:</h3> 
<p style='font-size:120%'>Since the null hypothesis is rejected, we can conclude that for a significance of 5% there is atleast one difference between means.</p>

<p style='font-size:120%'>APA writeup F(2, 12) = 9.75, p < 0.05, η2 (Effect size)= 0.62</p>

# Problem Statement 3:

Calculate F Test for given 10, 20, 30, 40, 50 and 5,10,15, 20, 25.

For 10, 20, 30, 40, 50:

$\text{Formula for standard deviation is }=\sqrt{\frac{1}{N - 1}\sum_{i=1}^N(x_i-\bar{x})^2}$

$\underline{\text{For first set,}}$

$\text{Inputs: (10, 20, 30, 40, 50)}$ 

$\text{Total inputs: 5}$

$\text{Formula for mean is} \frac{1}{n}\sum_{i=1}^{n} i = \frac{10 + 20 + 30 + 40 + 50}{5} = 30 $

$\begin{equation}SD = \sqrt{\frac{1}{5 - 1}(10 - 30)^{2} + (20 - 30)^{2} + (30 - 30)^{2} + (40 - 30)^{2} + (50 - 30)^{2}} = 15.8114\end{equation}$

$Variance = SD^{2} = 15.8114^{2} = 250$ 

$\underline{\text{For second set,}}$

$\text{Inputs: (5,10,15, 20, 25)}$ 

$\text{Total inputs: 5}$

$\text{Formula for mean is} \frac{1}{n}\sum_{i=1}^{n} i = \frac{5 + 10 + 15 + 20 + 25}{5} = 15 $

$\begin{equation}SD = \sqrt{\frac{1}{5 - 1}(5 - 15)^{2} + (10 - 15)^{2} + (15 - 15)^{2} + (20 - 15)^{2} + (25 - 15)^{2}} = 7.9057\end{equation}$

$Variance = SD^{2} = 7.9057^{2} = 62.5$ 

$\underline{\text{To calculate F−value: }}$

$\begin{equation}F−value = \frac{Variance_{\text{first test}}}{Variance_{\text{first test}}} = \frac{250}{62.5} = 4\end{equation}$

<p style='font-size:120%'>F−value is <b>4</b></p>
