import { useState, useEffect } from "react";
import "./App.css";
import BarChart from "./components/BarChart";
import LineChart from "./components/LineChart";
import PieChart from "./components/PieChart";
import { UserData } from "./Data";
import { palette } from '@mui/system';
import { Box, ThemeProvider } from '@mui/system';
import { AppBar, Toolbar, Typography } from '@mui/material';
import Logo from './logo.png';
import ResponsiveAppBar from './ResponsiveAppBar';


function App() {
  const [userData, setUserData] = useState({
    labels: UserData.map((data) => data.year),
    datasets: [
      {
        label: "",
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

  const [programmersData, setProgrammersData] = useState({
    labels: [],
    datasets: [
      {
        label: "Users Gained",
        data: [],
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

  useEffect(() => {
    const URL =
      "https://0h7pzyxz08.execute-api.us-east-2.amazonaws.com/default/get_pay";
    fetch(URL, {
      headers: {
        Accept: "application/json",
      },
    })
      .then((res) => res.json())
      .then((data) =>
        setProgrammersData({
          labels: data.map((data) => data.CompanyName),
          datasets: [
            {
              label: "Users Gained",
              data: data.map((data) => data.Pay),
              backgroundColor: [
                "rgba(75,192,192,1)",
                "#ecf0f1",
                "#50AF95",
                "#f3ba2f",
                "#2a71d0",
              ],
              borderColor: "black",
              borderWidth: 1,
            },
          ],
        })
      )
      .catch((err) => console.error(err));
  }, []);

  return (
    <div className="App">
      {/* <AppBar position="static">
        <Toolbar>
          <img src={Logo} alt="logo" style={{ marginRight: '1rem' }} />
          <Typography variant="h6" component="div">
            My React App
          </Typography>
        </Toolbar>
      </AppBar> */}

      <ResponsiveAppBar/>

      <Box
        display="flex"
        justifyContent="center"
        alignItems="center"
        minHeight="50vh"
      >
        <div style={{ width: 700 }}>
          <BarChart chartData={userData}/>
        </div>
      </Box>
        <main className="App-main">
          <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="50vh"
          >
            <div style={{ width: 700 }}>
              <BarChart chartData={userData}/>
            </div>
          </Box>
          <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="50vh"
          >
            <div style={{ width: 700 }}>
              <LineChart chartData={userData}/>
            </div>
          </Box>
          <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="50vh"
          >
            <div style={{ width: 700 }}>
              <PieChart chartData={userData}/>
            </div>
          </Box>
          <Box
          display="flex"
          justifyContent="center"
          alignItems="center"
          minHeight="50vh"
          >
            <div style={{ width: 1900 }}>
              <BarChart chartData={programmersData}/>
            </div>
          </Box>
        </main>
    </div>
  );
}


export default App;