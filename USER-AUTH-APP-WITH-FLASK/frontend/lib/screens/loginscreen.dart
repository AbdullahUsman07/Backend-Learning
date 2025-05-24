

import 'package:flutter/material.dart';
import 'package:frontend/widgets/customButton.dart';
import 'package:frontend/widgets/customTextFeild.dart';

class LoginUserScreen extends StatefulWidget {
  const LoginUserScreen({super.key});

  @override
  State<LoginUserScreen> createState() => _LoginUserScreenState();
}

class _LoginUserScreenState extends State<LoginUserScreen> {

  final TextEditingController nameController = TextEditingController();
  final TextEditingController passController = TextEditingController();


  @override
  void dispose() {
    nameController.dispose();
    passController.dispose();
    super.dispose();
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(  
      appBar: AppBar(  
        title: const Text('Login User'),
        centerTitle: true,
      ),
      body:Padding(padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 15),
        child: ListView(
          children: [
            CustomTextField(labelText: 'sername', controller: nameController, keyboardType: TextInputType.text),
            const SizedBox(height: 10),
            CustomTextField(labelText: 'password',controller: passController, keyboardType: TextInputType.text),
            const SizedBox(height: 20),
            CustomButton(onPressed: (){}, title: 'Login'),
          ],
        ),
      ),
    );
  }
}