import React, { Component } from 'react'
import { View } from 'react-native'
import { Button } from 'react-native-elements'
import deviceStorage from "../services/deviceStorage";

export default class HomeScreen extends Component {
  async removeJWT() {
    await deviceStorage.unsetJWT();
    deviceStorage.getJWT().then((jwt) => {
          console.log(jwt)
    })
    this.props.navigation.navigate('Login')

    deviceStorage.getJWT().then((jwt) => {
        console.log(jwt)
    })
    console.log("Not good")
  }

  logout() {
    console.log("Let's logout !");
      deviceStorage.getJWT().then((jwt) => {
          console.log(jwt)
      })
    this.removeJWT().catch((error) => {
        console.log(error);
    })
  }

  render() {
    return (
      <View style={{ flex: 1, alignItems: 'center', justifyContent: 'space-around' }}>
        <Button
          icon={{
            name: 'image',
            size: 40,
            color: 'white'
          }}
          title="Logout"
          onPress={() =>
            this.logout()
          }
          titleStyle={{ fontWeight: "700", fontSize: 60 }}
          buttonStyle={{
            backgroundColor: "#fec72f",
            width: 200,
            height: 70,
            borderColor: "transparent",
            borderWidth: 0,
            borderRadius: 50
          }}
        />
      </View>
    )
  }
}
