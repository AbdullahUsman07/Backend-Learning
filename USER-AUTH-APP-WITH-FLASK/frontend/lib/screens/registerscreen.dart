

import 'package:flutter/material.dart';
import 'package:frontend/widgets/customButton.dart';
import 'package:frontend/widgets/customTextFeild.dart';

class RegisterUserScreen extends StatefulWidget {
  const RegisterUserScreen({super.key});

  @override
  State<RegisterUserScreen> createState() => _RegisterUserScreenState();
}

class _RegisterUserScreenState extends State<RegisterUserScreen> {

  final TextEditingController nameController = TextEditingController();
  final TextEditingController passController = TextEditingController();
  final TextEditingController ageController = TextEditingController();

  @override
  void dispose() {
    nameController.dispose();
    passController.dispose();
    ageController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(  
      appBar: AppBar(  
        title: const Text('Register User'),
        centerTitle: true,
      ),
      body: Padding(
        padding: const EdgeInsets.symmetric(vertical: 10, horizontal: 15),
        child: ListView(
          children: [
            CustomTextField(labelText: 'Username', controller: nameController, keyboardType: TextInputType.text),
            const SizedBox(height: 10),
            CustomTextField(labelText: 'Password', controller: passController, keyboardType: TextInputType.text),
            const SizedBox(height: 10),
            CustomTextField(labelText: 'Age', controller: ageController, keyboardType: TextInputType.numberWithOptions(),),
            const SizedBox(height:20),
            CustomButton(onPressed: (){}, title: 'Register'),
          ],
        ),
      ),
    );
  }
}

