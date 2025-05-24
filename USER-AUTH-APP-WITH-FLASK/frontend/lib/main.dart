import 'package:flutter/material.dart';
import 'package:frontend/screens/homescreen.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'USER AUTHENTICATION APP',
      theme: ThemeData(primaryColor: Colors.purple),
      home: HomeScreen(),
    );
  }
}
