import React from 'react';
import {
  Chart as ChartJS,
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend,
} from 'chart.js';
import { Radar } from 'react-chartjs-2';

ChartJS.register(
  RadialLinearScale,
  PointElement,
  LineElement,
  Filler,
  Tooltip,
  Legend
);

function RadarChart({ chartData }) {
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      yAxes: [
        {
          ticks: {
            beginAtZero: true,
          },
        },
      ],
    },
    // datasets 내에 backgroundColor 속성을 추가하여 색상을 변경합니다.
    // chartData.datasets는 배열입니다. 여러 개의 레이더 차트를 표시하려면 각 레이더 차트에 대한 색상 배열을 추가할 수 있습니다.
    datasets: [
      {
        backgroundColor: ['rgba(255, 99, 132, 0.2)', 'rgba(54, 162, 235, 0.2)', 'rgba(255, 206, 86, 0.2)'],
      },
    ],
  };

  return <Radar data={chartData} options={options} />;
}

export default RadarChart;
