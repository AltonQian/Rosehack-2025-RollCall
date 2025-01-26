// async function getInsight() {
//     const response = await fetch('http://127.0.0.1:5000', {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json',
//       },
//       body: JSON.stringify({ schedule: userSchedule }),
//     });
  
//     const data = await response.json();
//     if (data.error) {
//       console.error("Error:", data.error);
//       return;
//     }
  
//     document.getElementById('insight').innerText = data.insight;
//   }
//   window.onload = getInsight;

