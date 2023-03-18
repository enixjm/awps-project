import React from 'react';
import { Bar } from 'react-chartjs-2';

function LanguageTable({ data }) {
  const chartData = {
    labels: Object.keys(data),
    datasets: [
      {
        label: 'Number of Users',
        data: Object.values(data),
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

  return (
    <div style={{ display: 'flex', justifyContent: 'center', alignItems: 'center', flexDirection: 'column', height: '100vh' }}>
      <h2 style={{ marginBottom: '20px' }}>Language Popularity</h2>
      <div style={{ width: '50%', marginBottom: '40px' }}>
        <Bar data={chartData} />
      </div>
      <table style={{ borderCollapse: 'collapse', border: '2px solid #ddd', width: '50%' }}>
        <thead>
          <tr style={{ backgroundColor: '#f2f2f2', fontWeight: 'bold' }}>
            <th style={{ border: '2px solid #ddd', padding: '8px' }}>Language</th>
            <th style={{ border: '2px solid #ddd', padding: '8px' }}>Users</th>
          </tr>
        </thead>
        <tbody>
          {Object.entries(data).map(([language, users], index) => (
            <tr key={language} style={{ backgroundColor: index % 2 === 0 ? '#f2f2f2' : 'transparent' }}>
              <td style={{ border: '2px solid #ddd', padding: '8px' }}>{language}</td>
              <td style={{ border: '2px solid #ddd', padding: '8px' }}>{users}</td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}



export default LanguageTable;