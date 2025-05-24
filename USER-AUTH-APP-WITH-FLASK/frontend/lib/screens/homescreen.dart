

import 'package:flutter/material.dart';
import 'package:frontend/screens/loginscreen.dart';
import 'package:frontend/screens/registerscreen.dart';
import 'package:frontend/widgets/customButton.dart';

class HomeScreen extends StatelessWidget {
  const HomeScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(  
      appBar: AppBar(  
        title: const Text('Home Screen'),
        centerTitle: true
      ),
      body: SizedBox(
        width: double.infinity,
        height: double.infinity,
        child: Padding(
          padding: const EdgeInsets.symmetric(horizontal: 20,vertical: 10),
          child: Column(  
            children: [
              CustomButton(title: 'Register', onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context)=> RegisterUserScreen()));
              },),
              const SizedBox(height:10),
              CustomButton(title: 'Login', onPressed: (){
                Navigator.push(context, MaterialPageRoute(builder: (context) =>  LoginUserScreen(),));
              },),
            ],
          )
          ),
      )
    );
  }
}

