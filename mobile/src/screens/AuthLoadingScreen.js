import React, {Component} from 'react';
import {
    ActivityIndicator,
    StatusBar,
    View,
} from 'react-native';
import styles from './styles'
import deviceStorage from '../services/deviceStorage'

export default class AuthLoadingScreen extends Component {
    constructor(props) {
        super(props);
        this.bootstrapAuth();
    }

    bootstrapAuth () {
        deviceStorage.getJWT().then((userToken) => {
            console.log("hey");
            this.props.navigation.navigate(userToken ? 'App' : 'Login');
        });
    };

    render() {
        return (
            <View style={styles.container}>
                <ActivityIndicator />
                <StatusBar barStyle="default" />
            </View>
        );
    }
}