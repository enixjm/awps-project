import { useState } from 'react';
import { Tabs, Tab, Box } from '@mui/material';

import BarChart from "./BarChart";
import LineChart from "./LineChart";
import PieChart from "./PieChart";
import Career_dataChart from "./Career_dataChart"
import { UserData } from "./Data";
import { useCareerData } from "./CareerData";
import { useEffect } from "react";

function MyTabs() {
  const [value, setValue] = useState(0);
  const handleChange = (event, newValue) => {
    setValue(newValue);
  };

  const [userData, setUserData] = useState({
    labels: UserData.map((data) => data.year),
    datasets: [
      {
        label: "Users Gained",
        data: UserData.map((data) => data.userGain),
        backgroundColor: [
          "rgba(75,192,192,1)",
          "#ecf0f1",
          "#50AF95",
          "#f3ba2f",
          "#2a71d0",
        ],
        borderColor: "black",
        borderWidth: 2,
      },
    ],
  });

  // const [careerData, setCareerData] = useState({
  //   labels: [],
  //   datasets: [
  //     {
  //       label: "Career Data",
  //       data: [],
  //       backgroundColor: [
  //         "rgba(75,192,192,1)",
  //         "#ecf0f1",
  //         "#50AF95",
  //         "#f3ba2f",
  //         "#2a71d0",
  //       ],
  //       borderColor: "black",
  //       borderWidth: 2,
  //     },
  //   ],
  // });
  
  // useEffect(() => {
  //   const URL =
  //     "https://gg9gosio9k.execute-api.us-east-2.amazonaws.com/default/get_PayAverage";
  //   fetch(URL, {
  //     headers: {
  //       Accept: "application/json",
  //     },
  //   })
  //     .then((res) => res.json())
  //     .then((data) =>
  //       setCareerData({
  //         labels: data.map((data) => data.CompanyName),
  //         datasets: [
  //           {
  //             label: "Users Gained",
  //             data: data.map((data) => data.Pay),
  //             backgroundColor: [
  //               "rgba(75,192,192,1)",
  //               "#ecf0f1",
  //               "#50AF95",
  //               "#f3ba2f",
  //               "#2a71d0",
  //             ],
  //             borderColor: "black",
  //             borderWidth: 1,
  //           },
  //         ],
  //       })
  //     )
  //     .catch((err) => console.error(err));
  // }, []);

  const careerData = useCareerData();
  const careerChartData = {
    labels: careerData.map((data) => data.CompanyName),
    datasets: [
      {
        label: "Average Salary",
        data: careerData.map((data) => data.Career),
        backgroundColor: [
          "rgba(75,192,192,1)",
          "#ecf0f1",
          "#50AF95",
          "#f3ba2f",
          "#2a71d0",
        ],
        borderColor: "black",
        borderWidth: 2,
      },
    ],
  };

  return (
    <Box sx={{
      width: '80%',
    }}>
      <Tabs value={value} onChange={handleChange} centered>
        <Tab label="BarChart" />
        <Tab label="LineChart" />
        <Tab label="PieChart" />
        <Tab label="Chart" />
      </Tabs>
      {value === 0 && <BarChart chartData={userData}/>}
      {value === 1 && <LineChart chartData={userData}/>}
      {value === 2 && <PieChart chartData={userData}/>}
      {value === 4 && <Career_dataChart chartData={careerData}/>} 
    </Box>
  );
}

export default MyTabs;