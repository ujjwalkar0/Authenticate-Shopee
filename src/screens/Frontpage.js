import  React from 'react';
import {StyleSheet, TouchableOpacity, View, Text, ImageBackground} from 'react-native';
import  Constants from 'expo-constants';
import * as Animatable from 'react-native-animatable';
// import CLogin from '../screens/CustomerLogin';
// import CRegister from '../screens/CustomerRegister';
// import SLogin from '../screens/ShopownerLogin';
// import SRegister from '../screens/ShopownerRegister';
// import DLogin from '../screens/DeliveryboyLogin';
// import DRegister from '../screens/DeliveryboyRegister';

export default class Front extends React.Component{
    render(){
    return (<View style= {styles.container}>
            <ImageBackground source={require('../images/live.gif')}
             style={{width:"100%",height:"130%", position:'absolute'}}
            />
            <Animatable.Text animation='fadeInDownBig' iterationCount="1" style={styles.header}>
                Authenticate Shopee
                </Animatable.Text>
            <Animatable.View animation='fadeInUpBig' iterationCount="1"  style={styles.footer}>
            <TouchableOpacity onPress={()=>{
                console.log('PRESSED');

            }}>
            <View style={styles.buttonContainer1}>
            <a href="CLogin"><Text style={styles.buttonText1}>
                SHOP OWNER
            </Text></a>
            </View>

            </TouchableOpacity>
            <TouchableOpacity onPress={()=>{
                console.log('PRESSED');
            }}>
            <View style={styles.buttonContainer2}>
            <Text style={styles.buttonText2}>
                CUSTOMER
            </Text>
            </View>

            </TouchableOpacity>
            <TouchableOpacity onPress={()=>{
                console.log('PRESSED');
            }}>
            <View style={styles.buttonContainer3}>
            <Text style={styles.buttonText3}>
                DELIVERY BOY
            </Text>
            </View>
            </TouchableOpacity>
            </Animatable.View>
            </View>
    ) 
}
};

const styles=StyleSheet.create({
    container:{
        marginTop: Constants.statusBarHeight
    },
    buttonContainer1: {
        height: 45,
        marginHorizontal: 100,
        marginTop: 220,
        backgroundColor: 'black',
        borderRadius: 50,
        borderWidth: 10,
        borderColor: 'black',
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonText1: {
        textTransform: 'uppercase',
        color: 'lime',
        fontSize: 18.5,
        fontWeight: 'bold'
    },
    buttonContainer2: {
        height: 45,
        marginHorizontal: 100,
        marginTop: 80,
        backgroundColor: 'black',
        borderRadius: 50,
        borderWidth: 10,
        borderColor: 'black',
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonText2: {
        textTransform: 'uppercase',
        color: 'lime',
        fontSize: 18.5,
        fontWeight: 'bold'
    },
    buttonContainer3: {
        height: 45,
        marginHorizontal: 100,
        marginTop: 80,
        backgroundColor: 'black',
        borderRadius: 50,
        borderWidth: 10,
        borderColor: 'black',
        justifyContent: 'center',
        alignItems: 'center'
    },
    buttonText3: {
        textTransform: 'uppercase',
        color: 'lime',
        fontSize: 18.5,
        fontWeight: 'bold'
    },
    header: {
        fontSize:30,
        fontFamily:"semiBold",
        marginTop:130,
        alignSelf:"center",
        fontWeight: '600'
        
    },
    footer: {

    }

});