import React from 'react';
import { Bar } from 'react-chartjs-2';

function LanguageTable({ data }) {
  const sortedData = Object.entries(data).sort((a, b) => b[1] - a[1]);
  const slicedData = sortedData.slice(0, 14)
  const chartData = {
    labels: slicedData.map(([label, value]) => label),
    datasets: [
      {
        label: 'Number of Users',
        data: slicedData.map(([label, value]) => value),
        backgroundColor: [
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
          'rgba(255, 99, 132, 0.2)',
          'rgba(54, 162, 235, 0.2)',
          'rgba(255, 206, 86, 0.2)',
          'rgba(75, 192, 192, 0.2)',
          'rgba(153, 102, 255, 0.2)',
          'rgba(255, 159, 64, 0.2)',
        ],
        borderColor: [
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
          'rgba(255, 99, 132, 1)',
          'rgba(54, 162, 235, 1)',
          'rgba(255, 206, 86, 1)',
          'rgba(75, 192, 192, 1)',
          'rgba(153, 102, 255, 1)',
          'rgba(255, 159, 64, 1)',
        ],
        borderWidth: 1,
      },
    ],
  };

  const chartOptions = {
    maintainAspectRatio: false,
    indexAxis: 'y',
  };

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column', }}>
      <h1 style={{ marginBottom: '40px', marginTop: '0px'}}>기술스택 강함순위 TOP14</h1>
      <div style={{ width: '100%', height: '700px' }}>
        <Bar data={chartData} options={chartOptions}/>
      </div>
    </div>
  );
}


export default LanguageTable;