<script>
  import * as Plot from "@observablehq/plot";
  import { onMount } from "svelte";
  import "../app.css";

  let chartContainer;
  let { data = [], class: className = "" } = $props();

  function renderChart() {
    if (!chartContainer) return;

    // Clear previous chart
    chartContainer.innerHTML = "";

    // Get container dimensions
    const containerWidth = chartContainer.clientWidth;
    const containerHeight = chartContainer.clientHeight;

    const chartPadding = 0.1; // 10% padding
    const chartMinValue = Math.min(...data.map((d) => d.value));
    const chartMaxValue = Math.max(...data.map((d) => d.value));

    const plot = Plot.plot({
      width: containerWidth,
      height: containerHeight,
      marginTop: 20,
      marginRight: 20,
      marginBottom: 20,
      marginLeft: 30,
      x: {
        type: "time",
        tickFormat: "%H:%M",
        grid: false,
        tickSize: 0,
        tickPadding: 0,
        color: "var(--color-foreground)",
      },
      y: {
        grid: true,
        tickSize: 0,
        tickPadding: 8,
        color: "var(--color-foreground)",
        domain: [
          chartMinValue - Math.abs(chartMinValue * chartPadding),
          chartMaxValue + Math.abs(chartMaxValue * chartPadding),
        ],
      },
      marks: [
        Plot.line(data, {
          x: "date",
          y: "value",
          stroke: "var(--color-foreground)",
          strokewidth: 2,
          curve: "monotone-x",
          title: (d) => `${d.date.toLocaleString()}\n${d.value.toFixed(2)}`,
        }),
      ],
    });
    chartContainer.appendChild(plot);
  }

  $effect(() => {
    renderChart();

    // Handle resize
    const resizeObserver = new ResizeObserver(renderChart);
    resizeObserver.observe(chartContainer);

    return () => {
      resizeObserver.disconnect();
    };
  });
</script>

<div bind:this={chartContainer} class={className}></div>
