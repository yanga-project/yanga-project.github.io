# yanga-project

```{toctree}
:hidden:
tools
logbook
```

{.lede}
A software product line engineering platform. Tools, workflows and trainings for building one product line into many variants on many platforms.

<div class="notes"><b>NOTES</b>
<ol>
<li>One configuration in, every variant out.</li>
</ol>
</div>

<!-- Process diagram: inputs merge into the pipeline, which fans out per variant and platform. -->
<svg class="diagram wide" viewBox="0 0 1080 300" role="img" aria-label="Process diagram: components, variants and platforms go through feature model, build system and build, and come out as one build per variant and platform">
  <g>
    <rect class="box" x="10" y="20" width="150" height="50"/><text x="22" y="50" font-size="13">components/</text>
    <rect class="box" x="10" y="125" width="150" height="50"/><text x="22" y="155" font-size="13">variants/</text>
    <rect class="box" x="10" y="230" width="150" height="50"/><text x="22" y="260" font-size="13">platforms/</text>
  </g>
  <path class="pipe" d="M160 45 H210 V150 M160 150 H260 M160 255 H210 V150"/>
  <g>
    <rect class="box" x="260" y="120" width="160" height="60"/><text x="272" y="146" font-size="12">Feature Model</text><text x="272" y="166" font-size="10" fill-opacity=".6">select features</text>
    <rect class="box" x="460" y="120" width="160" height="60"/><text x="472" y="146" font-size="12">Build System</text><text x="472" y="166" font-size="10" fill-opacity=".6">generate per variant</text>
    <rect class="box" x="660" y="120" width="150" height="60"/><text x="672" y="146" font-size="12">Build</text><text x="672" y="166" font-size="10" fill-opacity=".6">binaries, reports</text>
  </g>
  <path class="pipe" d="M420 150 H460 M620 150 H660 M810 150 H850 M850 40 V260 M850 40 H900 M850 110 H900 M850 190 H900 M850 260 H900"/>
  <g font-size="12">
    <text x="910" y="44">Variant A · Platform 1</text>
    <text x="910" y="114">Variant A · Platform 2</text>
    <text x="910" y="194">Variant B · Platform 1</text>
    <text x="910" y="264">… · …</text>
  </g>
  <g class="balloon" font-size="12">
    <line x1="540" y1="120" x2="565" y2="70"/><circle cx="577" cy="58" r="14"/><text x="573" y="62">2</text>
  </g>
</svg>

<!-- Same diagram, drawn top to bottom for narrow screens. -->
<svg class="diagram narrow" viewBox="0 0 360 540" role="img" aria-label="Process diagram: components, variants and platforms go through feature model, build system and build, and come out as one build per variant and platform">
  <g font-size="13">
    <rect class="box" x="4" y="10" width="110" height="44"/><text x="14" y="37">components/</text>
    <rect class="box" x="125" y="10" width="110" height="44"/><text x="135" y="37">variants/</text>
    <rect class="box" x="246" y="10" width="110" height="44"/><text x="256" y="37">platforms/</text>
  </g>
  <path class="pipe" d="M59 54 V78 H301 V54 M180 54 V110"/>
  <g font-size="14">
    <rect class="box" x="80" y="110" width="200" height="56"/><text x="96" y="135">Feature Model</text><text x="96" y="155" font-size="11" fill-opacity=".6">select features</text>
    <rect class="box" x="80" y="196" width="200" height="56"/><text x="96" y="221">Build System</text><text x="96" y="241" font-size="11" fill-opacity=".6">generate per variant</text>
    <rect class="box" x="80" y="282" width="200" height="56"/><text x="96" y="307">Build</text><text x="96" y="327" font-size="11" fill-opacity=".6">binaries, reports</text>
  </g>
  <path class="pipe" d="M180 166 V196 M180 252 V282 M180 338 V362 H40 V510 M40 390 H70 M40 430 H70 M40 470 H70 M40 510 H70"/>
  <g font-size="14">
    <text x="80" y="395">Variant A · Platform 1</text>
    <text x="80" y="435">Variant A · Platform 2</text>
    <text x="80" y="475">Variant B · Platform 1</text>
    <text x="80" y="515">… · …</text>
  </g>
  <g class="balloon" font-size="12">
    <line x1="280" y1="224" x2="310" y2="224"/><circle cx="324" cy="224" r="14"/><text x="320" y="228">2</text>
  </g>
</svg>

<table class="parts" aria-label="Parts list">
<tr><th>Item</th><th>Group</th><th>Part</th><th>Where</th></tr>
<tr><td>1</td><td>Tools</td><td>yanga-core, product line concepts</td><td><a href="tools.html">Sheet 2</a></td></tr>
<tr><td>2</td><td>Tools</td><td>yanga, build system backend for C/C++</td><td><a href="tools.html">Sheet 2</a></td></tr>
<tr><td>3</td><td>Workflows</td><td>How a team works with the tools</td><td>Not issued</td></tr>
<tr><td>4</td><td>Trainings</td><td>Hands-on product line engineering</td><td>Not issued</td></tr>
<tr><td>5</td><td>Examples</td><td>Product lines built on the platform</td><td>Not issued</td></tr>
<tr><td>6</td><td>Logbook</td><td>Notes from building the platform</td><td><a href="logbook.html">Sheet 6</a></td></tr>
</table>
